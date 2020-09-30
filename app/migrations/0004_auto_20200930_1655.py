# Generated by Django 3.1.1 on 2020-09-30 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_invoice_invoiceline'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitemmovement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2012-02-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitemmovement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='app.invitemcategory'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_master', to='app.itemmasterdata'),
        ),
        migrations.AlterField(
            model_name='invitemmovement',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='move_item_master', to='app.itemmasterdata'),
        ),
        migrations.AlterField(
            model_name='vendorpostingsetup',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_posting', to='app.invitemcategory'),
        ),
        migrations.AlterField(
            model_name='vendorpostingsetup',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_posting', to='app.vendorpostinggroup'),
        ),
    ]