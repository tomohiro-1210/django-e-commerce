from django.urls import path
from .views import item_views, cart_views, pay_views, account_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('top/', item_views.IndexListView.as_view()),
    # 商品詳細
    path('items/<str:pk>/', item_views.ItemDetailView.as_view()),
    
    # カート
    path('cart/', cart_views.CartListView.as_view()),
    # カート追加
    path('cart/add/', cart_views.AddCartView.as_view()),
    # カート削除
    path('cart/remove/<str:pk>/', cart_views.remove_from_cart),
    
    # Stripe決済
    path('pay/checkout/', pay_views.PayWithStripe.as_view()),
    path('pay/success/', pay_views.PaySuccessView.as_view()),
    path('pay/cancel/', pay_views.PayCancelView.as_view()),
    
    # アカウント関連
    path('login/', account_views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', account_views.SignUpView.as_view()),
    path('account/', account_views.AccountUpdateView.as_view()),
    path('profile/', account_views.ProfileUpdateView.as_view()),
    
]
