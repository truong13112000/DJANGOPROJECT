from django.shortcuts import render
from django.urls import reverse
from flask import redirect

import pandas as pb
import numpy as np
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
import login

from login.models import Account

def get_home(request):
    return render(request,'login.html')

def getdata():
    df = pb.read_csv

@api_view(['POST'])
def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        authen = authenticate(request, username=username, password=password)
        print('User is '+ str(authen))
        user = Account.objects.filter(username=username).first()
        isCheckPass = check_password(password, user.password)
        if isCheckPass is True:
            request.session['accout_id'] = user.id
            request.session.save()
            account_id_session = request.session['accout_id']
            print('account_id_session is' + str(account_id_session))
            return redirect('get_home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')