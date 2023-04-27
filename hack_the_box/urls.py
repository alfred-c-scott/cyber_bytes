from django.urls import path
from .views import HackTheBoxHomeView

app_name = 'hack_the_box'
urlpatterns = [
    path('', HackTheBoxHomeView.as_view(), name='hack_the_box_home')
    ]
