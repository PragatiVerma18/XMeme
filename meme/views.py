from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Meme
from .serializers import MemeSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
