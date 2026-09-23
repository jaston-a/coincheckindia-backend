from rest_framework import serializers
from .models import Category, CoinOrNoteVariant

class CoinOrNoteVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinOrNoteVariant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    variants = CoinOrNoteVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'item_type', 'variants']