from django.urls import path
from .views import KeepaHomeView

app_name = 'keepa'
urlpatterns = [
    path('', KeepaHomeView.as_view(), name='keepa_home')
    ]
