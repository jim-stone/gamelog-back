from rest_framework.serializers import ModelSerializer
from .models import GameRegistered


class GameRegisteredSerializer(ModelSerializer):
    class Meta:
        model = GameRegistered
        fields = ('bga_id', 'name', 'description', 'thumb_url')
