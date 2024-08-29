from django.urls import path
from .views import item_views, cart_views

urlpatterns = [
    path('top/', item_views.IndexListView.as_view()),
    # 商品詳細
    path('items/<str:pk>/', item_views.ItemDetailView.as_view()),
    # カート
    path('cart/', cart_views.CartListView.as_view()),
    # カート追加
    path('cart/add/', cart_views.AddCartView.as_view()),
    # カート削除
    path('cart/remove/<str:pk>/', cart_views.remove_from_cart)
]
