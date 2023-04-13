from django.db import models

from django.db import models

class Product_Upload_Result (models.Model):
    id = models.AutoField(primary_key=True)
    session_no = models.IntegerField(null=False)
    total_record =  models.IntegerField(null=False)
    title = models.CharField(max_length=255,null=True) 
    ng_record = models.IntegerField(null=True)
    ok_record = models.IntegerField(null=True)
    file_upload_path = models.CharField(max_length=255,null=True) 
    file_discuss_upload_path = models.CharField(max_length=255,null=True) 
    c_date = models.DateTimeField(null=False)
    u_date = models.DateTimeField(null=False)
    is_file_upload = models.BooleanField(null=False,default=False)
    u_user = models.IntegerField(null=True)
    is_upload = models.BooleanField(null=False,default=False)
    vendor_code = models.CharField(max_length=255,null=True) 
    screen_type = models.CharField(max_length=10,null=True) 
    md_ids_selected = models.JSONField(null=True) 
    status = models.CharField(max_length=1,null=True) 
    account_id = models.BigIntegerField(null=True)
    c_year_month =  models.CharField(max_length=6,null=True)
    discussion_no = models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'product_upload_result'
