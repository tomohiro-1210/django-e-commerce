from django.contrib import admin
from .models.item_models import *
from django.contrib.auth.models import Group, User

# タグを選びやすくする
class TagInline(admin.TabularInline):
    model = Item.tags.through
    
class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']

# 管理画面で表示させるモデル
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# 管理画面で非表示にさせるモデル
# admin.site.unregister(Group)
# admin.site.unregister(User)