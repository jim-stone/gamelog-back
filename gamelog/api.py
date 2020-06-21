from rest_framework.routers import DefaultRouter
from games import api_views as games_views

router = DefaultRouter()
router.register(r'games', games_views.GameRegisteredViewSet)
