from rest_framework import serializers
from app import models
from django.db import transaction


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

class GeneralBuisnessPostingSetupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeneralBuisnessPostingSetup
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

class InvoiceLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceLine
        fields = '__all__'
        read_only_fields = ("invoice", "tax",)

class InvoiceSerializer(serializers.ModelSerializer):

    invoice_invoiceline = InvoiceLineSerializer(many=True)

    class Meta:
        model = models.Invoice
        fields = '__all__'
        read_only_fields = ("sub_total", "total_tax", "total")

    @transaction.atomic
    def create(self, validated_data):
        invoice, invoice_lines = self.calculate_total_amount_and_vat(validated_data)
        invoice = models.Invoice.objects.create(**invoice)

        for invoice_line in invoice_lines:
            invoice_li = models.InvoiceLine.objects.create(invoice=invoice, **invoice_line)

        return invoice

    @transaction.atomic
    def update(self, instance, validated_data):
        invoice, invoice_line_data = self.calculate_vat(validated_data)
        invoice_lines = list((instance.invoice_invoiceline).all())

        for nested_data in invoice_line_data:
            line_instance = invoice_lines.pop(0)
            line_instance.item = nested_data.get("item", line_instance.item)
            line_instance.quantity = nested_data.get("quantity", line_instance.quantity)
            line_instance.tax = nested_data.get("tax", line_instance.tax)
            line_instance.save()

        return super(InvoiceSerializer, self).update(instance, invoice)

    def calculate_total_amount_and_vat(self, invoice_data):
        invoice_lines = invoice_data.pop("invoice_invoiceline")
        total = 0
        vat = 0
        for invoice_line in invoice_lines:
            vat_amount = invoice_line.get("item").vat_posting_group.vat/100
            unit_price = invoice_line.get("item").unit_price
            total_amount = invoice_line.get("quantity")*unit_price
            total_vat = total_amount * vat_amount
            total = total + total_amount
            vat = vat + total_vat

            invoice_line["tax"] = total_vat

        invoice_data["sub_total"] = total
        invoice_data["total_tax"] = vat
        invoice_data["total"] = total + vat

        return invoice_data, invoice_lines







