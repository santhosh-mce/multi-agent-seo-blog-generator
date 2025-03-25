import time
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from seo_blog_generator.settings import GEMINI_API_KEY

# Initialize the Gemini chat model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)
last_request_time = 0
request_interval = 30  # Time gap between requests to avoid rate limits

def generate_content(outline):
    global last_request_time
    content = ""

    for section in outline["sections"]:
        prompt = f"Write a detailed section about {section['heading']} for an HR blog post. Use professional and engaging language."
        
        # Ensure rate limiting
        current_time = time.time()
        if current_time - last_request_time < request_interval:
            wait_time = request_interval - (current_time - last_request_time)
            print(f"Waiting {wait_time:.1f} seconds to avoid rate limiting...")
            time.sleep(wait_time)
        
        # Retry mechanism for API failures
        max_retries = 3
        retry_delay = 5  # Delay in seconds between retries
        for attempt in range(max_retries):
            try:
                response = model.invoke([HumanMessage(content=prompt)])
                section["content"] = response.content if hasattr(response, "content") else str(response)

                # Format without <h2> or <h3>, use <strong> for emphasis
                content += f"{section['heading']}\n{section['content']}\n"
                last_request_time = time.time()  # Update last request time
                break  # Exit retry loop if successful
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)  # Wait before retrying
                else:
                    section["content"] = f"Failed to generate content for {section['heading']} due to API error."
                    content += f"{section['heading']}\n{section['content']}\n"

    return content
