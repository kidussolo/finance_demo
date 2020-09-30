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

class ChartsOfAccount_LA(generics.ListCreateAPIView):
    queryset = models.ChartsOfAccount.objects.all()
    serializer_class = serializers.ChartsOfAccountSerializer

class ChartsOfAccount_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ChartsOfAccount.objects.all()
    serializer_class = serializers.ChartsOfAccountSerializer
    lookup_field = "id"

class UnitOfMeasurement_LA(generics.ListCreateAPIView):
    queryset = models.UnitOfMeasurement.objects.all()
    serializer_class = serializers.UnitOfMeasurementSerializer

class UnitOfMeasurement_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UnitOfMeasurement.objects.all()
    serializer_class = serializers.UnitOfMeasurementSerializer
    lookup_field = "id"

class InvItemLocation_LA(generics.ListCreateAPIView):
    queryset = models.InvItemLocation.objects.all()
    serializer_class = serializers.InvItemLocationSerializer

class InvItemLocation_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InvItemLocation.objects.all()
    serializer_class = serializers.InvItemLocationSerializer
    lookup_field = "id"

class ItemCategory_LA(generics.ListCreateAPIView):
    queryset = models.InvItemCategory.objects.all()
    serializer_class = serializers.InvItemCategorySerializer

class ItemCategory_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InvItemCategory.objects.all()
    serializer_class = serializers.InvItemCategorySerializer
    lookup_field = "id"
    
class Items_LA(generics.ListCreateAPIView):
    queryset = models.InventoryItem.objects.all()
    serializer_class = serializers.InventoryItemSerializer

class Items_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InventoryItem.objects.all()
    serializer_class = serializers.InventoryItemSerializer
    lookup_field = "id"

class ItemsMasterData_LA(generics.ListCreateAPIView):
    queryset = models.ItemMasterData.objects.all()
    serializer_class = serializers.ItemMasterDataSerializer

class ItemsMasterData_RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ItemMasterData.objects.all()
    serializer_class = serializers.ItemMasterDataSerializer
    lookup_field = "id"
    