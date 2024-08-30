from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from ecapp.models import Profile
from ecapp.forms import UserCreationForm

# ユーザー登録
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'pages/login_signup.html'
 
    def form_valid(self, form):
        return super().form_valid(form)
    
# ユーザー画面
class Login(LoginView):
    template_name = 'pages/login_signup.html'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
# アカウントプロフィール更新？
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email')
    success_url = '/account/'
    
    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
    
# プロフィール更新
class  ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'pages/profile.html'
    fields = ('name', 'zipcode', 'prefecture', 'city', 'address1', 'address2', 'tel')
    success_url = '/profile/'
    
    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()