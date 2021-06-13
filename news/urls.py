from django.urls import path

from .views import *

urlpatterns = [
    path('', LinkCreate.as_view()),
    path('all/', lib)
]