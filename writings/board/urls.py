from django.urls import path
from .views import board_view, post_message

urlpatterns = [
    path('', board_view, name='board'),
    path('post/', post_message, name='post_message'),
]
