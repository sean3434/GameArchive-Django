from django.db import models

LIST_CHOICES = (
    ('want to play','Want To Play'),
    ('currently playing', 'Currently Playing'),
    ('finished playing','Finished Playing'),
    ('stopped playing','Stopped Playing'),
)

class Game(models.Model):

    title = models.CharField(max_length=100)
    cover_art = models.CharField(max_length=250)
    release_date = models.DateField
    developer = models.TextField(max_length=100)
    rating = models.TextField(max_length=3)
    platform = models.TextField(max_length=100)
    genre = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    add_to_list = models.CharField(max_length=17, choices=LIST_CHOICES, default='finished playing')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
