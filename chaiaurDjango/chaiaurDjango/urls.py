"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include # include is imported to include other URL configurations
from django.conf import settings
from django.conf.urls.static import static #this static tell to load media which we creted in settings.py
# This is the main URL configuration for the chaiaurDjango project.
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),
    path('chai/', include('chai.urls')),  # Include the URLs from the chai app
    
    
    path('__reload__/', include('django_browser_reload.urls')),  # For live reloading during development
    # the above is the path that makes tailwind hot reload possible
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# why we use above line is because we want to serve media files during development
# The above line ensures that media files are served correctly during development.
# If you are using Django's development server, it will automatically serve static files.