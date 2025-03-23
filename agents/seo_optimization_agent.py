from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from seo_blog_generator.settings import GEMINI_API_KEY

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)

def optimize_seo(content, topic):
    # Generate SEO keywords
    keyword_prompt = f"Generate 5 high-ranking SEO keywords for a blog post about '{topic}'. Return them as a comma-separated list."
    
    keyword_response = model.invoke([HumanMessage(content=keyword_prompt)])
    keywords = keyword_response.content.split(", ") if hasattr(keyword_response, "content") else []

    # Optimize content with keywords
    optimized_content = content
    for keyword in keywords:
        optimized_content = optimized_content.replace(keyword, f"<strong>{keyword}</strong>")

    return optimized_content, keywords
