# Generated by Django 4.1 on 2023-04-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Upload_Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_no', models.IntegerField(unique=True)),
                ('total_record', models.IntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
                ('ng_recor', models.IntegerField(null=True)),
                ('ok_record', models.IntegerField(null=True)),
                ('file_upload_path', models.CharField(max_length=255, null=True)),
                ('file_discuss_upload_path', models.CharField(max_length=255, null=True)),
                ('c_date', models.DateTimeField()),
                ('u_date', models.DateTimeField()),
                ('is_file_upload', models.BooleanField(default=False)),
                ('u_user', models.IntegerField(null=True)),
                ('is_upload', models.BooleanField(default=False)),
                ('vendor_code', models.CharField(max_length=255, null=True)),
                ('screen_type', models.CharField(max_length=10, null=True)),
                ('md_ids_selected', models.JSONField(null=True)),
                ('status', models.CharField(max_length=1, null=True)),
                ('account_id', models.BigIntegerField(null=True)),
                ('c_year_month', models.CharField(max_length=6, null=True)),
                ('discussion_no', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'product_upload_result',
            },
        ),
    ]
