from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    last_login = models.DateTimeField(null=True)
    is_superuser = models.BooleanField(default=False,null=True)
    username = models. CharField(max_length=150,null=True)
    first_name =  models. CharField(max_length=150,null=True)
    last_name = models. CharField(max_length=150,null=True)
    is_staff = models.BooleanField(default=False,null=True)
    is_active = models.BooleanField(default=False,null=True)
    date_joined = models.DateTimeField(null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=255,null=True)
    update_date = models.DateTimeField(null=True)
    is_first_login = models.BooleanField(default=False,null=True)
    md_code = models.CharField(max_length=255,null=True)
    is_admin = models.BooleanField(default=False,null=True)
    max_user = models.IntegerField(null=True)
    count_user = models.IntegerField(null=True)
    create_by_id = models.BigIntegerField(null=True)
    
    class Meta:
        db_table = 'account'