from django.db import IntegrityError
from rest_framework.serializers import ModelSerializer
from .models import GameRegistered, PlayerGame


class GameRegisteredSerializer(ModelSerializer):
    class Meta:
        model = GameRegistered
        fields = ('bga_id', 'name', 'description', 'thumb_url')

    def create(self, validated_data):

        user = self.context['request'].user
        game_exists = GameRegistered.objects.filter(
            name=validated_data.get('name')
        ).first()  # avoids DNE Error without try/except clause

        if game_exists:
            try:
                self._create_player_game_relation(
                    player=user.userplayer,
                    game=game_exists)
            except IntegrityError:
                print('No new object. Integrity error explicitly silenced')
            else:
                print('New PlayerGame object created')
            finally:
                print(PlayerGame.objects.all())
                return game_exists

        new_game = super().create(validated_data)
        self._create_player_game_relation(
            player=user.userplayer,
            game=new_game)
        print(PlayerGame.objects.all())
        return new_game

    def _create_player_game_relation(self, player, game):
        PlayerGame.objects.create(player=player, game=game)


class PlayerGameSerializer(ModelSerializer):
    class Meta:
        model = PlayerGame
        fields = ('game', 'player')
