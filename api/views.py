from .serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Category, Product

class CategoryDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
