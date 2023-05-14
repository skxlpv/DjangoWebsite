from django.urls import path

from info.views import MusicianViewSet

urlpatterns = [
    path('musician/', MusicianViewSet.as_view({'get': 'list'}), name='musician'),
]
