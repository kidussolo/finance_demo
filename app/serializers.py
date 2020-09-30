from rest_framework import serializers
from app import models


class ChartsOfAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChartsOfAccount
        fields = '__all__'

class UnitOfMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UnitOfMeasurement
        fields = '__all__'

class ItemMasterDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ItemMasterData
        fields = '__all__'

class InvItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvItemCategory
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InventoryItem
        fields = '__all__'

class InvItemMovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvItemMovement
        fields = '__all__'

class VendorPostingGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VendorPostingGroup
        fields = '__all__'

class VendorPostingSetupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VendorPostingSetup
        fields = '__all__'

class VatPostingGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VatPostingGroup
        fields = '__all__'

class VatPostingSetupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VatPostingSetup
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vendor
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Journal
        fields = '__all__'

class InvItemLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvItemLocation
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invoice
        fields = '__all__'

class InvoiceLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceLine
        fields = '__all__'