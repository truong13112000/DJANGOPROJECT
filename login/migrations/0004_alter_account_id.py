# Generated by Django 4.1 on 2023-04-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_account_count_user_alter_account_create_by_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
