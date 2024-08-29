from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from ecapp.models import Item

# TOPページに表示する商品リスト
class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'
    
# 商品詳細ページ
class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'