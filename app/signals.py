from datetime import datetime
from app import models

def record_journal_transactions(sender, instance, **kwargs):
    if instance.state == "validated":
        description = "some item purchase"
        date_time = datetime.now()
        invoice_lines = instance.invoice_invoiceline.all()
        print(invoice_lines)
        vendor_posting_group = instance.vendor.vendor_posting_group
        jounral_entry = models.JournalEntryLine.objects.create(
            Journal=instance.journal,
            date = date_time,
            description=description,
            amount=instance.total,
            account=models.ChartsOfAccount.objects.get(id=1)
        )

def get_entry_accounts(self, invoice_lines, vendor_posting_group):
    """
    return which account should be involved in the transaction
    """
    accounts = []
    for invoice_line in invoice_lines:
        product_posting_group = invoice_line.item.category
        # account lookup
        print(product_posting_group)
        acct = get_matching_account(vendor_posting_group, product_posting_group)
        accounts.append(acct)

    pass

def get_matching_account(self, vendor_posting_group, item_posting_group):
    """
    return the matching account from the vendor posting setup
    """
    account = models.VendorPostingSetup.objects.filter(i)
