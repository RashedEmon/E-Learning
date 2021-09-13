
from django.urls import path, include

from .views import add_post_view, index, add_subject, Subject_List_View, topic_list_by_subject_view, add_topic_view, add_post_view, user_list_view


urlpatterns = [
    path('', index),
    path('subject/add', add_subject, name="subject-add"),
    path('subjects/', Subject_List_View, name="subject-list"),
    path('topiclist/', topic_list_by_subject_view, name="topic-list-xhr"),
    path('addTopic/', add_topic_view, name="add-topic"),
    path('addPost/', add_post_view, name="add-post"),
    path('users/', user_list_view, name="user-list"),
]

