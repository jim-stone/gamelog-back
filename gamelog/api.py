from rest_framework.routers import DefaultRouter
from games import api_views as games_views

app_name = 'games'
router = DefaultRouter()
router.register(r'games', games_views.GameRegisteredViewSet)
router.register(r'playergames', games_views.PlayerGameViewSet,
                basename='playergame')
