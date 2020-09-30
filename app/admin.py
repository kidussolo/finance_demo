from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.ChartsOfAccount)
admin.site.register(models.Journal)
admin.site.register(models.UnitOfMeasurement)
admin.site.register(models.Vendor)
admin.site.register(models.InvItemLocation)
admin.site.register(models.InventoryItem)
admin.site.register(models.ItemMasterData)
admin.site.register(models.Invoice)
admin.site.register(models.InvoiceLine)
admin.site.register(models.VatPostingSetup)
admin.site.register(models.VendorPostingSetup)
admin.site.register(models.InvItemMovement)
admin.site.register(models.InvItemCategory)
admin.site.register(models.VendorPostingGroup)
admin.site.register(models.VatPostingGroup)
