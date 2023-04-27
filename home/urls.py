from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ResumePageView

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    ]
