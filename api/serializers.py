from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'name', 'description', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('id', 'category', 'name', 'description', 'link', 'image', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
