from rest_framework import generics
from django.db.models import Q
from .models import Category, CoinOrNoteVariant
from .serializers import CategorySerializer, CoinOrNoteVariantSerializer

# Home page categories (5 Paisa, 1 Rupee, etc.)
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Detail view of a single coin/note variant
class CoinVariantDetailView(generics.RetrieveAPIView):
    queryset = CoinOrNoteVariant.objects.all()
    serializer_class = CoinOrNoteVariantSerializer

# Search API (Search by Year or Title)
class CoinSearchListView(generics.ListAPIView):
    serializer_class = CoinOrNoteVariantSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return CoinOrNoteVariant.objects.filter(
                Q(title__icontains=query) | 
                Q(year__icontains=query) | 
                Q(description__icontains=query)
            )
        return CoinOrNoteVariant.objects.none()