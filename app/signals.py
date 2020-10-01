from datetime import datetime
from app import models

def record_journal_transactions(sender, instance, created, **kwargs):
    if created:
        description = "some item purchase"
        date_time = datetime.now()
        journal = instance.invoice.journal
        jounral_entry = models.JournalEntry.objects.create(
            journal=journal,
            date = date_time,
            description=description
        )



    pass