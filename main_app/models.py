from django.db import models
from django.contrib.auth.models import User

LIST_CHOICES = (
    ('want to play','Want To Play'),
    ('currently playing', 'Currently Playing'),
    ('finished playing','Finished Playing'),
    ('stopped playing','Stopped Playing'),
)

class Game(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    cover_art = models.CharField(max_length=250, blank=True, null=True)
    release_date = models.DateField(blank=True)
    developer = models.CharField(max_length=101, blank=True, null=True)
    rating = models.CharField(max_length=3, blank=True, null=True)
    platform = models.CharField(max_length=102, blank=True, null=True)
    genre = models.CharField(max_length=103, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    add_to_list = models.CharField(max_length=17, choices=LIST_CHOICES, default='finished playing', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     favorite_color = models.CharField(max_length=50)