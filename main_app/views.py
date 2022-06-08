from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Landing(TemplateView):
    template_name = "landing.html"

class Home(TemplateView):
    template_name = "home.html"