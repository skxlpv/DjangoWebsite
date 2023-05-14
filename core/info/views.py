from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from info.models import MusicianModel
from info.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = MusicianModel.objects.all()
    serializer_class = MusicianSerializer

    def create(self, request, *args, **kwargs):
        pass
