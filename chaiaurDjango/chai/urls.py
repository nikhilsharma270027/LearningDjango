from django.urls import path
from . import views

# localhost:8000/chai
# This file defines the URL patterns for the chai app.
urlpatterns = [
    path('', views.all_chai, name='all_home'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]
# The above code defines the URL patterns for the chai app, mapping URLs to views.