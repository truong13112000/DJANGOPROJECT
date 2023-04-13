from django.shortcuts import render

from product.models import Product_Upload_Result
from django.db import connections

def get_home(request):
    product = get_data_table(request)
    print(str(product))
    return render(request,'product.html',{'product': product})

def get_data_table(request):
    account_id_session = request.session['accout_id']
    print('tets' +str(account_id_session))
    if account_id_session is not None:
        cursor = connections['default'].cursor()
        cursor.execute("""
            SELECT a.discussion_no,b.email,a.title
            FROM public.product_upload_result a
            left join public.account as b on a.account_id = b.id
            WHERE a.account_id = 11;
        """)
        results = cursor.fetchall()
        print(str(results))
    return results