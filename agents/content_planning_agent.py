# agents/content_planning_agent.py

def create_outline(topic):
    """
    Creates a structured outline for the blog post with headings and subheadings.
    """
    outline = {
        "title": f"Trending HR Topic: {topic}",
        "sections": [
            {
                "heading": "Introduction",
                "subheadings": [
                    "Overview of the Topic",
                    "Why It Matters in HR"
                ],
                "content": ""
            },
            {
                "heading": "Key Trends and Insights",
                "subheadings": [
                    "Recent Developments",
                    "Industry Best Practices",
                    "Challenges and Solutions"
                ],
                "content": ""
            },
            {
                "heading": "Implementation Strategies",
                "subheadings": [
                    "How Companies Can Adapt",
                    "Case Studies and Examples"
                ],
                "content": ""
            },
            {
                "heading": "Conclusion",
                "subheadings": [
                    "Key Takeaways",
                    "Future Outlook"
                ],
                "content": ""
            }
        ]
    }
    return outline
