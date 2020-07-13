from rest_framework import viewsets, permissions
from .models import GameRegistered
from .serializers import GameRegisteredSerializer


class GameRegisteredViewSet(viewsets.ModelViewSet):
    queryset = GameRegistered.objects.all()
    serializer_class = GameRegisteredSerializer


class PlayerGameViewSet(viewsets.ModelViewSet):

    serializer_class = GameRegisteredSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        player = self.request.user.userplayer
        queryset = GameRegistered.objects.filter(player_games__player=player)
        return queryset
