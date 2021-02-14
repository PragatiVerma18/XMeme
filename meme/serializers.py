from rest_framework import serializers
from . import models


class MemeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'url', 'caption')
        model = models.Meme
