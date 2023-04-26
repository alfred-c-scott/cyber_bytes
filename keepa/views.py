from django.shortcuts import render
from django.views.generic import TemplateView


class KeepaHomeView(TemplateView):
    template_name = 'keepa/keepa_home.html'
