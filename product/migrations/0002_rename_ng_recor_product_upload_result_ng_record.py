# Generated by Django 4.1 on 2023-04-12 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_upload_result',
            old_name='ng_recor',
            new_name='ng_record',
        ),
    ]
