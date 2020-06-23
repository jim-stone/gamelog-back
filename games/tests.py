# import json
from django.test import TestCase
from django.test import Client
# from rest_framework.test import APIClient as Client
# from rest_framework.authtoken.models import Token
# from rest_framework import status
# from django.urls import reverse
from django.contrib.auth.models import User
from .models import GameRegistered, PlayerGame, UserPlayer

# Create your tests here.

client = Client()
TOKEN_URL = '/api/auth/token/login/'


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


class LoginApiTest(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='kuba', password='kuba')

    def test_01_can_get_login_token(self):
        response = client.post(
            path=TOKEN_URL,
            data={'username': 'kuba', 'password': 'kuba'},
            content_type='application/json'
        )
        self.assertEquals(response.status_code, 200)
        self.assertIn('auth_token', response.json())

    def test_02_no_access_unless_authenticated(self):
        url = '/api/games/'
        response = client.get(url)
        self.assertEquals(response.status_code, 401)


class GameRegistrationSerializerTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='kuba', password='kuba')
        GameRegistered.objects.create(name='Colt Express')
        GameRegistered.objects.create(name='7 wonders')
        self.token = client.post(
            path=TOKEN_URL,
            data={'username': 'kuba', 'password': 'kuba'},
            content_type='application/json'
        ).json()['auth_token']
        # client.login(username='kuba', password='kuba').json()
        # self.token = Token.objects.all()
        # print(self.token)
        # client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_01_can_get_games_via_api(self):
        url = '/api/games/'
        response = client.get(
            url, **{'HTTP_AUTHORIZATION': f'Token {self.token}'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 2)
