from django.shortcuts import render
from .models import BlogPost
from agents.research_agent import find_trending_hr_topics
from agents.content_planning_agent import create_outline
from agents.content_generation_agent import generate_content
from agents.seo_optimization_agent import optimize_seo
from agents.review_agent import review_content
from django.conf import settings
from django.shortcuts import get_object_or_404, render
import os

from django.http import HttpResponse
import markdown
import pdfkit
from django.utils.text import slugify

def generate_blog(request):
    topics = find_trending_hr_topics()  # ✅ Define `topics` at the start
    
    if request.method == 'POST':
        topic = request.POST.get('topic')
        outline = create_outline(topic)
        content = generate_content(outline)
        optimized_content, keywords = optimize_seo(content, topic)
        reviewed_content = review_content(optimized_content)
        
        blog_post = BlogPost.objects.create(
            title=outline["title"],
            content=reviewed_content,
            seo_keywords=", ".join(keywords)
        )
        

        return render(request, 'blog/generate_blog.html', {'topics': topics, 'blog_post': blog_post})  # ✅ Now `topics` is always defined

    return render(request, 'blog/generate_blog.html', {'topics': topics})

def index(request):
    """
    Renders the index (home) page of the application.
    """
    return render(request, 'blog/index.html')



def save_blog(request, post_id):
    # Fetch the blog post
    blog_post = get_object_or_404(BlogPost, id=post_id)
    
    # Create the file content
    file_content = f"# {blog_post.title}\n{blog_post.content}"
    
    # Define the file name
    file_name = f"{slugify(blog_post.title)}.md"  # Save as .md file
    # file_name = f"{slugify(blog_post.title)}.txt"  # Save as .txt file
    
    # Create an HTTP response with the file
    response = HttpResponse(file_content, content_type='text/markdown')  # For .md
    # response = HttpResponse(file_content, content_type='text/plain')  # For .txt
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    
    return response

