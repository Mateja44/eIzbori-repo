from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
import random
from django.db.models import Count
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpRequest, Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth import get_user_model
from Process.models import *
from datetime import datetime

# Create your views here.

def login_user(request, licence):
    korisnik = get_object_or_404(CustomUser, licence=licence)
    licence_value = korisnik.licence
    first_name = korisnik.first_name
    last_name = korisnik.last_name

    context = {
        'licence': licence_value,
        'first_name': first_name,
        'last_name': last_name
    }

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(email=email, sifra=password)
            #user = CustomUser.objects.get(email=email, sifra=password) Moze samo jedan argument !!!
            if user:
                login(request, user)
                return redirect(f'listic/{licence}')
            else:
                messages.error(request, 'Wrong Password Or User')
        except:
            messages.error(request, 'User Does Not Exist')
    return render(request, 'login_registration.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    return HttpResponse('Register')

def listic(request, licence):

    user = get_object_or_404(CustomUser, licence=licence)
    licence_value = user.licence
    first_name = user.first_name
    last_name = user.last_name
    regionalni = user.regional_section
    maticni = user.local_section

    size = CustomUser.objects.aggregate(count=Count('licence'))['count']

    random_list = []
    for i in range(size):
        r = random.randint(1, 100000)
        if r not in random_list:
            random_list.append(r)
    
    users = CustomUser.objects.values('first_name', 'last_name', 'licence')
    full_names = [f"{user['first_name']} {user['last_name']} {user['licence']}" for user in users]
        
    context = {
        'licence': licence_value,
        'first_name': first_name,
        'last_name': last_name,
        'regionalni': regionalni,
        'maticni': maticni,
        'full_names': full_names,
    }

    return render(request, 'listic.html', context)

def hvala(request):
    return render(request, 'hvala.html')

def send_email(request, licence):

    user = get_object_or_404(CustomUser, licence=licence)
    mail = user.email
    first_name = user.first_name
    last_name = user.last_name
    pswd = "xuqumizscvldnrgo"
    smtp_port = 587                 
    smtp_server = "smtp.gmail.com" 
    from_email = 'agandr456@gmail.com'

    if request.method == 'POST':

        subject = 'Uspesno glasanje'
        body = f'{first_name} {last_name}\n Uspesno ste glasali. Hvala.'
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = mail
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()

        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(from_email, pswd)
        TIE_server.sendmail(from_email, mail, text)
        TIE_server.quit()

    return render(request, 'hvala.html')
