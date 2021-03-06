# Generated by Django 4.0.5 on 2022-06-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_art', models.CharField(blank=True, max_length=250)),
                ('release_date', models.DateField(blank=True)),
                ('developer', models.CharField(blank=True, max_length=100)),
                ('rating', models.CharField(blank=True, max_length=3)),
                ('platform', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('add_to_list', models.CharField(choices=[('want to play', 'Want To Play'), ('currently playing', 'Currently Playing'), ('finished playing', 'Finished Playing'), ('stopped playing', 'Stopped Playing')], default='finished playing', max_length=17)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
