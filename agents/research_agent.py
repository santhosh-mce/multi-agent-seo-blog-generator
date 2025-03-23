import time
import ast
import json
import logging
from django.core.cache import cache
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from seo_blog_generator.settings import GEMINI_API_KEY

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)

# Rate limiting variables
last_request_time = 0
request_interval = 30  # Minimum interval between requests (in seconds)
cache_key = "trending_hr_topics"
cache_timeout = 60 * 60  # Cache for 1 hour

def find_trending_hr_topics():
    global last_request_time

    # Check cache first
    cached_topics = cache.get(cache_key)
    if cached_topics:
        logging.info("Returning cached HR topics.")
        return cached_topics

    prompt = (
        "List 5 trending HR topics for 2025 in Python list format, without explanations. "
        "Example: ['Topic1', 'Topic2', 'Topic3', 'Topic4', 'Topic5']"
    )

    # Rate limiting: Ensure at least `request_interval` seconds between requests
    current_time = time.time()
    if current_time - last_request_time < request_interval:
        wait_time = request_interval - (current_time - last_request_time)
        logging.info(f"Waiting {wait_time:.1f} seconds to avoid rate limiting...")
        time.sleep(wait_time)

    # Retry mechanism for rate limiting
    max_retries = 3
    retry_delay = 5  # Delay in seconds between retries
    for attempt in range(max_retries):
        try:
            response = model.invoke([HumanMessage(content=prompt)])
            response_text = response.content.strip() if hasattr(response, "content") else str(response).strip()

            logging.info("Response from Gemini: %s", response_text)

            # Ensure response is properly formatted as a Python list
            try:
                topics = ast.literal_eval(response_text)
                if isinstance(topics, list) and all(isinstance(topic, str) for topic in topics):
                    last_request_time = time.time()  # Update last request time
                    cache.set(cache_key, topics, timeout=cache_timeout)  # Store in cache
                    return topics
            except (SyntaxError, ValueError):
                logging.warning("Failed to parse response, returning fallback topics.")

            # If parsing fails, return fallback topics
            return ["Remote Work", "Employee Well-being", "Hybrid Work Models", "AI in HR", "Diversity and Inclusion"]

        except Exception as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)  # Wait before retrying
            else:
                # Fallback topics if all retries fail
                return ["Remote Work", "Employee Well-being", "Hybrid Work Models", "AI in HR", "Diversity and Inclusion"]
