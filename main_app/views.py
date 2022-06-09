from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Game

class Landing(TemplateView):
    template_name = "landing.html"

class Home(TemplateView):
    template_name = "home.html"

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'cover_art', 'release_date', 'developer', 'rating', 'platform', 'genre', 'description', 'add_to_list']
    template_name = "game_create.html"
    success_url = "/home/"

class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

class FinishedPlaying(TemplateView):
    template_name = "finished_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(add_to_list='finished playing')
        return context

class CurrentlyPlaying(TemplateView):
    template_name = "currently_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(add_to_list='currently playing')
        return context

class StoppedPlaying(TemplateView):
    template_name = "stopped_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(add_to_list='stopped playing')
        return context

class WantToPlay(TemplateView):
    template_name = "want_to_play.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(add_to_list='want to play')
        return context