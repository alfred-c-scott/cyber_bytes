from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ResumePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('home/', HomePageView.as_view(), name='home'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    ]