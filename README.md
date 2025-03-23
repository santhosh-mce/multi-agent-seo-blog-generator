<h1 align="center"> System Architecture </h1>

The project follows a multi-agent system (MAS) architecture, where each agent is responsible for a different aspect of blog generation. The agents collaborate to produce well-structured and optimized content.

![alt text](<image/System architecture.jpg>)

<br/>
Each agent in the system has a specific role, including:

<ul>
  <li><strong>Content Analysis Agent</strong>: Analyzes topic relevance and trends.</li>
  <li><strong>Writing Agent</strong>: Generates structured content with coherence.</li>
  <li><strong>Optimization Agent</strong>: Enhances SEO and readability.</li>
  <li><strong>Review Agent</strong>: Ensures grammar accuracy and fact-checking.</li>
  <li><strong>Publishing Agent</strong>: Formats and publishes the content.</li>

</ul>

This modular approach ensures efficient blog generation with high-quality output.
<br/>
<br/>

<h1 align="center">Workflow</h1>

<ul>
        <li><strong>Topic Research:</strong> The Research Agent fetches trending HR-related topics.</li>
        <li><strong>Outline Creation:</strong> The Content Planning Agent structures the blog post.</li>
        <li><strong>Content Writing:</strong> The Content Generation Agent writes detailed sections.</li>
        <li><strong>SEO Optimization:</strong> The SEO Optimization Agent enhances content for search engines.</li>
        <li><strong>Final Review:</strong> The Review Agent proofreads and ensures quality content.</li>
        <li><strong>Output Generation:</strong> The final blog post is saved as a .txt or .md file for further use.</li>
    </ul>
<br/>


<h1 align="center">Tools & Frameworks</h1>

<ul>
        <li><strong>Markdown:</strong> 3.7</li>
        <li><strong>pdfkit:</strong> 1.0.0</li>
        <li><strong>langchain:</strong> 0.0.200</li>
        <li><strong>langchain-core:</strong> 0.2.43</li>
        <li><strong>langchain-google-genai:</strong> 1.0.10</li>
        <li><strong>Django:</strong> 4.2</li>
        <li><strong>Python</strong> (Main Language)</li>
        <li><strong>BeautifulSoup / Scrapy</strong> (Web Scraping for Trending Topics)</li>
        <li><strong>OpenAI API</strong> (Content Generation)</li>
        <li><strong>NLTK / Grammarly API</strong> (Text Processing and Proofreading)</li>
        <li><strong>SEO Analysis Tools</strong> (e.g., Yoast SEO API)</li>
    </ul>
<br/>


<h1 align="center">Installation & Execution</h1>

<h3>Prerequisites</h3>
Ensure you have the following installed:

<ul>
        <li>Python 3.11+</li>
        <li>Required Python packages (install using the command below)</li>
    </ul>


<h3>Setup Instructions</h3>


1. Clone the Repository:
```bash
  git clone https://github.com/santhosh-mce/multi-agent-seo-blog-generator.git
  cd multi-agent-seo-blog-generator
```
2. Create a Virtual Environment:
```bash
  python -m venv myenv 
  myenv\Scripts\activate   # On Windows
```
3. Install Dependencies:
```bash
  pip install -r requirements.txt 
```

4. Set Up API Keys (for OpenAI & Web Scraping):
<ul>
<li>Create a .env file in the root directory.</li>
<li>Add your API keys:</li>
</ul>

```bash
  OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the System:
```bash
  python manage.py runserver
```

