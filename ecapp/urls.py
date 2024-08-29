from django.urls import path
from .views import item_views

urlpatterns = [
    path('top/', item_views.IndexListView.as_view()),
    path('items/<str:pk>/', item_views.ItemDetailView.as_view()),
]
