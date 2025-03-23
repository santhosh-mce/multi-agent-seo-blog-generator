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



# def download_blog(request, post_id, format_type):
#     blog_post = get_object_or_404(BlogPost, id=post_id)

#     if format_type == "md":
#         response = HttpResponse(blog_post.content, content_type="text/markdown")
#         response["Content-Disposition"] = f'attachment; filename="{blog_post.title}.md"'
#         return response

#     elif format_type == "txt":
#         response = HttpResponse(blog_post.content, content_type="text/plain")
#         response["Content-Disposition"] = f'attachment; filename="{blog_post.title}.txt"'
#         return response

#     elif format_type == "html":
#         html_content = f"<h1>{blog_post.title}</h1><p>{blog_post.content}</p>"
#         response = HttpResponse(html_content, content_type="text/html")
#         response["Content-Disposition"] = f'attachment; filename="{blog_post.title}.html"'
#         return response


#     return HttpResponse("Invalid format", status=400)


