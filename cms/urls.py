from django.urls import path
from .views import *

urlpatterns = [
    path('add/',add_stories, name = "add_story"),
    path('stories/', stories, name = "stories"),
    path('about/', about, name = "about"),
    path('stories/<int:pk>/', StoryUpdateView.as_view(),name = "story"),
    path('story_detail/<int:pk>/', StoryDetailView.as_view(),name = "story_detail"),
    path('delete/<int:pk>/', StoryDeleteView.as_view(),name = "delete_story")
]


