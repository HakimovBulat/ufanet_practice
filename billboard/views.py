from django.shortcuts import render
from .models import Category, Sale
from django.db.models import Q


def index(request):
    if request.method == "POST":
        sale_search = request.POST.get("sale_search", "").lower()

        query = Q(title__icontains=sale_search)
        query.add(Q(subtitle__icontains=sale_search), Q.OR)
        query.add(Q(about_partner__icontains=sale_search), Q.OR)
        query.add(Q(description__icontains=sale_search), Q.OR)

        context = {
            "sales": Sale.objects.filter(query),
            "categories": [],
        }
    else:
        context = {
            "categories": Category.objects.all(),
            "sales": Sale.objects.all(),
        }
    return render(request, "billboard/index.html", context=context)


def category_sales(request, pk):
    category = Category.objects.get(pk=pk)

    context = {
        "category_title": category.title,
        "sales": category.sale_set.all()
    }
    return render(request, "billboard/category_sales.html", context=context)


def sale_info(request, sale_pk):
    context = {
        "sale": Sale.objects.get(pk=sale_pk)
    }
    return render(request, "billboard/sale_info.html", context=context)