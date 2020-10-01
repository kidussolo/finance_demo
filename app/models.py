from django.db import models
from django.db.models.signals import post_save
from app import signals



class ChartsOfAccount(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    account_number = models.IntegerField()
    report_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=50)
    short_form = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InvItemCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VatPostingGroup(models.Model):
    name = models.CharField(max_length=50)
    vat = models.IntegerField()
    grouping = models.ManyToManyField(
        "self",
        through='VatPostingSetup',
        through_fields=('vendor_vat', 'item_vat'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ItemMasterData(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(InvItemCategory, on_delete=models.CASCADE)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE)
    vat_posting_group = models.ForeignKey(VatPostingGroup, blank=True, null=True, on_delete=models.CASCADE)
    unit_price = models.FloatField(blank=True, null=True)
    total_quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InvItemLocation(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class InventoryItem(models.Model):
    item = models.ForeignKey(ItemMasterData, related_name="item_master", on_delete=models.CASCADE)
    category = models.ForeignKey(InvItemCategory, related_name="item_category", on_delete=models.CASCADE)
    location = models.ForeignKey(InvItemLocation, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item)



class InvItemMovement(models.Model):
    item = models.ForeignKey(ItemMasterData, related_name="move_item_master", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item)


class VendorPostingGroup(models.Model):
    name = models.CharField(max_length=50)
    grouping = models.ManyToManyField(
        InvItemCategory,
        through='VendorPostingSetup',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class VendorPostingSetup(models.Model):
    vendor = models.ForeignKey(VendorPostingGroup, related_name="vendor_posting", on_delete=models.CASCADE)
    item = models.ForeignKey(InvItemCategory, related_name="item_posting", on_delete=models.CASCADE)
    purchase_account = models.ForeignKey(ChartsOfAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vendor) + " mappied to " + str(self.item)

    


class VatPostingSetup(models.Model):
    vendor_vat = models.ForeignKey(VatPostingGroup, related_name="vendor_vat", on_delete=models.CASCADE)
    item_vat = models.ForeignKey(VatPostingGroup, related_name="item_vat", on_delete=models.CASCADE)
    vat_receivable = models.ForeignKey(ChartsOfAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vendor_vat) + " mappied to " + str(self.item_vat) 




class Vendor(models.Model):
    name = models.CharField(max_length=50)
    vendor_posting_group = models.ForeignKey(VendorPostingGroup, blank=True, null=True, on_delete=models.CASCADE)
    vat_posting_group = models.ForeignKey(VatPostingGroup, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    credit_limit = models.FloatField()
    debit_limit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    date = models.DateTimeField()
    sub_total = models.FloatField()
    total = models.FloatField()
    total_tax = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)

class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="invoice_invoiceline", on_delete=models.CASCADE)
    item = models.ForeignKey(ItemMasterData, related_name="item_master_data", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    tax = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item)

class JournalEntry(models.Model):
    date = models.DateTimeField()
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class JournalEntryLine(models.Model):
    journal_entry = models.ForeignKey(Journal, related_name="journal_entry", on_delete=models.PROTECT)
    amount = models.FloatField()
    account = models.ForeignKey(ChartsOfAccount, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

post_save.connect(signals.record_journal_transactions, sender=InvoiceLine)