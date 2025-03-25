from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from seo_blog_generator.settings import GEMINI_API_KEY

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)

def review_content(content):
    prompt = prompt = f"""
                        Review and improve this HR blog content while maintaining EXACTLY these 4 section headings:

                        Introduction
                        [content here]

                        Key Trends and Insights  
                        [content here]

                        Implementation Strategies
                        [content here]

                        Conclusion
                        [content here]

                        Focus on:
                        1. Grammar and clarity improvements
                        2. Enhancing readability and flow
                        3. Increasing engagement
                        4. SEO optimization

                        Provide the revised content with:
                        - All 4 original headings preserved exactly as shown above
                        - Each heading on its own line
                        - Improved content under each section
                        - Brief explanations of key changes

                        Original Content:
                        {content}

                        Revised Version:
                        """

    response = model.invoke([HumanMessage(content=prompt)])

    return response.content if hasattr(response, "content") else str(response)
