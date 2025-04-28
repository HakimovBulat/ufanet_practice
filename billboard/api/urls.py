from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path("sale/", views.SaleListView.as_view(), name="sale_list"),
    path("sale/<int:pk>/", views.SaleDetailView.as_view(), name="sale_detail"),
]