from rest_framework import serializers

from info.models import MusicianModel


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicianModel
        fields = ['name', ]
