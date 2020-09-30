from django.db import models


class ChartsOfAccount(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    report_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemPostingGroup(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemMasterData(models.Model):
    name = models.CharField(max_length=50)
    item_group = models.ForeignKey(ItemPostingGroup, on_delete=models.CASCADE)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InvItemCategory(models.Model):
    name = models.CharField(max_length=50)

class InventoryItem(models.Model):
    item = models.OneToOneField(ItemMasterData, on_delete=models.CASCADE)
    quantity = models.FloatField()
    category = models.ForeignKey(InvItemCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class InvItemMovement(models.Model):
    item = models.ForeignKey(ItemMasterData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()



class VendorPostingGroup(models.Model):
    name = models.CharField(max_length=50)
    grouping = models.ManyToManyField(
        ItemPostingGroup,
        through='VendorPostingSetup',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class VendorPostingSetup(models.Model):
    vendor = models.ForeignKey(VendorPostingGroup, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemPostingGroup, on_delete=models.CASCADE)
    purchase_account = models.ForeignKey(ChartsOfAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
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

class VatPostingSetup(models.Model):
    vendor_vat = models.ForeignKey(VatPostingGroup, related_name="vendor_vat", on_delete=models.CASCADE)
    item_vat = models.ForeignKey(VatPostingGroup, related_name="item_vat", on_delete=models.CASCADE)
    vat_receivable = models.ForeignKey(ChartsOfAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class vendor(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(VendorPostingGroup, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    credit_limit = models.FloatField()
    debit_limit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Journal(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)