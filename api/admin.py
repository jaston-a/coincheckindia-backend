from django.contrib import admin
from .models import Category, CoinOrNoteVariant

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CoinOrNoteVariant)
class CoinOrNoteVariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'mint_mark', 'rarity', 'estimated_value')
    list_filter = ('category', 'rarity', 'year')
    search_fields = ('title', 'description', 'mint_mark')