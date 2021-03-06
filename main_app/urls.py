from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('home/', views.Home.as_view(), name="home"),
    path('games/new/', views.GameCreate.as_view(), name="game_create"),
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_detail"),
    path('games/<int:pk>/update',views.GameUpdate.as_view(), name="game_update"),
    path('games/<int:pk>/delete',views.GameDelete.as_view(), name="game_delete"),
    path('library/stoppedplaying/', views.StoppedPlaying.as_view(), name="stopped_playing"),
    path('library/currentlyplaying/', views.CurrentlyPlaying.as_view(), name="currently_playing"),
    path('library/finishedplaying/', views.FinishedPlaying.as_view(), name="finished_playing"),
    path('library/wanttoplay/', views.WantToPlay.as_view(), name="want_to_play"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('games/search/', views.Search, name='search'),
    path('games/details/stop', views.Stop, name='stop'),
    path('games/details/current', views.Current, name='current'),
    path('games/details/finish', views.Finish, name='finish'),
    path('games/details/want', views.Want, name='want'),

]