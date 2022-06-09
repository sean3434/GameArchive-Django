from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('home/', views.Home.as_view(), name="home"),
    path('games/new/', views.GameCreate.as_view(), name="game_create"),
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_detail"),
    path('library/stoppedplaying/', views.StoppedPlaying.as_view(), name="stopped_playing"),
    path('library/currentlyplaying/', views.CurrentlyPlaying.as_view(), name="currently_playing"),
    path('library/finishedplaying/', views.FinishedPlaying.as_view(), name="finished_playing"),
    path('library/wanttoplay/', views.WantToPlay.as_view(), name="want_to_play"),
]