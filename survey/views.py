from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'


class TravelView(TemplateView):
    template_name = 'travel.html'


class ElementsView(TemplateView):
    template_name = 'elements.html'
