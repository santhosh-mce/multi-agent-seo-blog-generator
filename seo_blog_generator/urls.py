"""
URL configuration for seo_blog_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import generate_blog, index, save_blog, save_blog_html, save_blog_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),  # Map the root URL to the index view
    path('generate/', generate_blog, name='generate_blog'),
    path('md/<int:post_id>/', save_blog, name='save_blog'),
    path('html/<int:post_id>/', save_blog_html, name='save_blog_html'),
    path('pdf/<int:post_id>/', save_blog_pdf, name='save_blog_pdf'),
]
