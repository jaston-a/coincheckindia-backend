from django.urls import path
from .views import CategoryListView, CoinVariantDetailView, CoinSearchListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('coins/<int:pk>/', CoinVariantDetailView.as_view(), name='coin-detail'),
    path('search/', CoinSearchListView.as_view(), name='coin-search'),
]