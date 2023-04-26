from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/home.html'


class AboutPageView(TemplateView):
    template_name = 'home/about.html'


class ContactPageView(TemplateView):
    template_name = 'home/contact.html'


class ResumePageView(TemplateView):
    template_name = 'home/resume.html'
