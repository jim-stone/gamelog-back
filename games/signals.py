from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . import models


@receiver(post_save, sender=User)
def create_userplayer_handler(sender, instance, created,
                              dispatch_id="unique id to run once",
                              ** kwargs):
    if not created:
        return
    user_player = models.UserPlayer(user=instance)
    user_player.save()
