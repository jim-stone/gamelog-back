from rest_framework import viewsets

from .models import GameRegistered
from .serializers import GameRegisteredSerializer


class GameRegisteredViewSet(viewsets.ModelViewSet):
    queryset = GameRegistered.objects.all()
    serializer_class = GameRegisteredSerializer
