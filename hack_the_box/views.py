from django.views.generic import TemplateView


class HackTheBoxHomeView(TemplateView):
    template_name = 'hack_the_box/hack_the_box_home.html'
