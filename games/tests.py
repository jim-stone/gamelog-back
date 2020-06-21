from django.test import TestCase
from django.contrib.auth.models import User
from .models import GameRegistered, PlayerGame, UserPlayer

# Create your tests here.


class GameRegistrationTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='Adam')
        User.objects.create_user(username='Ania')
        User.objects.create_user(username='Kuba')
        GameRegistered.objects.create(name='Colt Express')
        GameRegistered.objects.create(name='7 Wonders')

    def test_00_always_pass(self):
        self.assertFalse(False)

    def test_01_creates_player_on_user_registration(self):
        # confirms that signal works
        player = UserPlayer.objects.get(user__username='Adam')
        self.assertEqual(str(player), 'Player Adam')

    def test_02_registers_game_with_player(self):
        player = UserPlayer.objects.get(user__username='Adam')
        game = GameRegistered.objects.get(name='Colt Express')
        PlayerGame.objects.create(player=player, game=game)
        game2 = GameRegistered.objects.get(name='7 Wonders')
        PlayerGame.objects.create(player=player, game=game2)
        games_list = [str(x) for x in player.games.all()]
        games_names = ['Player Adam knows Game Colt Express',
                       'Player Adam knows Game 7 Wonders']
        self.assertEqual(games_list, games_names)
