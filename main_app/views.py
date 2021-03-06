from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

from .models import Game

API_KEY = '2b3cce12bb324a6c91904de7b3790e97'

def Search(request):
    gametitle = request.GET.get('gametitle')
    url = f'https://api.rawg.io/api/games?search={gametitle}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    results = data['results']

    context = {
        'results' : results
    }
    return render(request, 'search.html', context)

class Landing(TemplateView):
    template_name = "landing.html"

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class GameCreate(CreateView):
    model = Game
    fields = ['title', 'cover_art', 'release_date', 'developer', 'rating', 'platform', 'genre', 'description', 'add_to_list']
    template_name = "game_create.html"
    success_url = "/home/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GameCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

@method_decorator(login_required, name='dispatch')
class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'cover_art', 'release_date', 'developer', 'rating', 'platform', 'genre', 'description', 'add_to_list']
    template_name = "game_update.html"
    success_url = "/library/currentlyplaying/"

@method_decorator(login_required, name='dispatch')
class GameDelete(DeleteView):
    model = Game
    template_name = "game_delete_confirmation.html"
    success_url = "/library/currentlyplaying/"

@method_decorator(login_required, name='dispatch')
class FinishedPlaying(TemplateView):
    template_name = "finished_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(user=self.request.user, add_to_list='finished playing')
        return context

@method_decorator(login_required, name='dispatch')
class CurrentlyPlaying(TemplateView):
    template_name = "currently_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(user=self.request.user, add_to_list='currently playing')
        return context

@method_decorator(login_required, name='dispatch')
class StoppedPlaying(TemplateView):
    template_name = "stopped_playing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(user=self.request.user, add_to_list='stopped playing')
        return context

@method_decorator(login_required, name='dispatch')
class WantToPlay(TemplateView):
    template_name = "want_to_play.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.filter(user=self.request.user, add_to_list='want to play')
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("library/currentlyplaying")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

def Stop(request):
    slug = request.GET.get('slug')
    url = f'https://api.rawg.io/api/games/{slug}?key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    game_data = Game(
            title = data['name'],
            cover_art = data['background_image'],
            release_date = data['released'],
            developer = data['developers'][0]['name'],
            rating = data['metacritic'],
            platform = 'PC',
            genre = data['genres'][0]['name'],
            description = data['description'],
            add_to_list = 'stopped playing',
            user = request.user
        )
    game_data.save()

    context = {
        'data' : data
    }
    return render(request, 'stop.html', context)

def Current(request):
    slug = request.GET.get('slug')
    url = f'https://api.rawg.io/api/games/{slug}?key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    game_data = Game(
            title = data['name'],
            cover_art = data['background_image'],
            release_date = data['released'],
            developer = data['developers'][0]['name'],
            rating = data['metacritic'],
            platform = 'PC',
            genre = data['genres'][0]['name'],
            description = data['description'],
            add_to_list = 'currently playing',
            user = request.user
        )
    game_data.save()

    context = {
        'data' : data
    }
    return render(request, 'current.html', context)

def Finish(request):
    slug = request.GET.get('slug')
    url = f'https://api.rawg.io/api/games/{slug}?key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    game_data = Game(
            title = data['name'],
            cover_art = data['background_image'],
            release_date = data['released'],
            developer = data['developers'][0]['name'],
            rating = data['metacritic'],
            platform = 'PC',
            genre = data['genres'][0]['name'],
            description = data['description'],
            add_to_list = 'finished playing',
            user = request.user
        )
    game_data.save()

    context = {
        'data' : data
    }
    return render(request, 'finish.html', context)

def Want(request):
    slug = request.GET.get('slug')
    url = f'https://api.rawg.io/api/games/{slug}?key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    game_data = Game(
            title = data['name'],
            cover_art = data['background_image'],
            release_date = data['released'],
            developer = data['developers'][0]['name'],
            rating = data['metacritic'],
            platform = 'PC',
            genre = data['genres'][0]['name'],
            description = data['description'],
            add_to_list = 'want to play',
            user = request.user
        )
    game_data.save()

    context = {
        'data' : data
    }
    return render(request, 'want.html', context)