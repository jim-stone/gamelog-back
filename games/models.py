from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GameRegistered (models.Model):
    bga_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    thumb_url = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class UserPlayer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Player {self.user.username}'


class PlayerGame(models.Model):
    game = models.ForeignKey(to=GameRegistered, on_delete=models.CASCADE)
    player = models.ForeignKey(
        to=UserPlayer, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return f'Player {self.player.user.username} knows Game {self.game.name}'
