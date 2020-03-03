#this is where we add our routes for a specific app
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'), #urls that use the path
    path('about/', views.about, name='blog-about'),
]