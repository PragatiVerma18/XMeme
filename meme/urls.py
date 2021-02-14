
from django.urls import path
from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter

from .views import MemeViewSet

router = SimpleRouter()
router.register('memes', MemeViewSet, basename='memes')

urlpatterns = router.urls
