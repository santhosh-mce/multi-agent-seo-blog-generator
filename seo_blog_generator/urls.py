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
from django.conf.urls import handler404
from django.urls import path
from blog.views import generate_blog, index, save_blog, save_blog_html, save_blog_pdf, custom_404
from django.conf import settings
from django.conf.urls.static import static


handler404 = custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),  # Map the root URL to the index view
    path('generate/', generate_blog, name='generate_blog'),
    path('md/<int:post_id>/', save_blog, name='save_blog'),
    path('html/<int:post_id>/', save_blog_html, name='save_blog_html'),
    path('pdf/<int:post_id>/', save_blog_pdf, name='save_blog_pdf'),
]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
