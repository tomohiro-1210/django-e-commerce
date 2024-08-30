from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from ecapp.models import Item
import stripe

# APIキー
stripe.api_key = settings.STRIPE_API_SECRET_KEY

# 決済成功
class PaySuccessView(TemplateView):
    template_name = 'pages/success.html'
    
    def get(self, request, *args, **kwargs):
        # 最新のOrderオブジェクトを取得し、注文確定に変更
        
        # カート情報削除
        del request.session['cart']
        
        return super().get(request, *args, **kwargs)
    
# キャンセル
class PayCancelView(TemplateView):
    template_name = 'pages\cancel.html'
    
    def get(self, request, *args, **kwargs):
        # 最新のOrderオブジェクトを取得
        
        # 在庫数と販売数をもとの状態に戻す
        
        # is_confirmedがFalseであれば削除
        
        
        return super().get(request, *args, **kwargs)

# 

# 
class PayWithStripe(View):
 
    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            return redirect('/')
 
        line_items = []
        for item_pk, quantity in cart['items'].items():
            item = Item.objects.get(pk=item_pk)
            line_item = create_line_item(
                item.price, item.name, quantity)
            line_items.append(line_item)
 
        checkout_session = stripe.checkout.Session.create(
            # customer_email=request.user.email,
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f'{settings.MY_URL}/pay/success/',
            cancel_url=f'{settings.MY_URL}/pay/cancel/',
        )
        return redirect(checkout_session.url)