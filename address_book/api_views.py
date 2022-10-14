from rest_framework import viewsets
from . import models
from . import serializers

class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer