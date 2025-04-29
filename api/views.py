from rest_framework import generics
from billboard.models import Sale, Category
from .serializers import SaleSerializer, CategorySerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SaleListView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


    @method_decorator(cache_page(60 * 15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


    @method_decorator(cache_page(60 * 15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)



class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @method_decorator(cache_page(60 * 15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @method_decorator(cache_page(60 * 15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)