from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from seo_blog_generator.settings import GEMINI_API_KEY

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)

def review_content(content):
    prompt = f"""Review the following blog content for grammar, readability, and engagement. 
    Suggest improvements if needed and provide a revised version with clear explanations:\n\n{content}"""

    response = model.invoke([HumanMessage(content=prompt)])

    return response.content if hasattr(response, "content") else str(response)
