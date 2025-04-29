from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(("api.urls", "api"), namespace="api")),
    path("billboard/", include(('billboard.urls', "billboard"), namespace="billboard"))
]
