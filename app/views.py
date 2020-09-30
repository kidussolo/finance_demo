from rest_framework import generics, status
from app import models
from app import serializers
from rest_framework.response import Response


class Journals_LA(generics.ListCreateAPIView):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer

class Journals_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer
    lookup_field = "id"
    
    