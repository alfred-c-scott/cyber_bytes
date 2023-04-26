from django.shortcuts import render
from django.views.generic import TemplateView


class QuizAppHomeView(TemplateView):
    template_name = 'quiz_app/quiz_app_home.html'
