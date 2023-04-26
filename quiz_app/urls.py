from django.urls import path
from .views import QuizAppHomeView

app_name = 'quiz_app'
urlpatterns = [
    path('', QuizAppHomeView.as_view(), name='quiz_app_home'),
    ]
