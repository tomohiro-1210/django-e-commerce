from django.urls import path
from .views import *

urlpatterns = [
    path('top/', item_views.IndexListView.as_view()),
]
