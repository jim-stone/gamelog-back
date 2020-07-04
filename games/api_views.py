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
        # print('User: ', self.request.user, self.request.user.userplayer)
        # queryset = GameRegistered.objects.all()
        queryset = GameRegistered.objects.filter(playergame__player=player)
        return queryset
