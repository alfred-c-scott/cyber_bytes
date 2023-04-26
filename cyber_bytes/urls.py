# cyber_bytes/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('hack_the_box/', include('hack_the_box.urls')),
    path('keepa/', include('keepa.urls')),
    path('quiz_app/', include('quiz_app.urls')),
    ]
