from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'


class TravelView(TemplateView):
    template_name = 'travel.html'


class ElementsView(TemplateView):
    template_name = 'elements.html'


class ThaiView(TemplateView):
    template_name = 'countries/thai.html'


class SriLankaView(TemplateView):
    template_name = 'countries/srilanka.html'


class PolandView(TemplateView):
    template_name = 'countries/poland.html'
