# cyber_bytes/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hack_the_box.urls")),
    ]
