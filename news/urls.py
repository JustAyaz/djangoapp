from django.urls import path

from .views import *

urlpatterns = [
    path('', LinkCreate.as_view()),
    path('all/', lib),
    path('new_link/', newLink, name="new_link"),
    path('<str:key>/', openLink, name="open_link"),
    path('delete/<int:pk>/', deleteOrder, name="delete_link")
]