from django.urls import path 
from . import views

urlpatterns = [
    path("<str:blog>",views.blog_display)
]

