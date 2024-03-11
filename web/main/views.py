import os
from requests import Session
import json
from .forms import ModelApiForm
import json
from json import JSONDecodeError
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'main/home_page.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # On enverra un email et on enregistrera dans la base de données (in progress)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirige vers la même page après l'envoi du message
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})


@login_required
def formulaire(request):
    api_url = os.environ.get('URL_API')
    

    if request.method == "POST":
        form = ModelApiForm(request.POST)
        if form.is_valid():
            try:
                headers = {'Content-Type': 'application/json'}
                # Conversion de l'objet date en chaîne de caractères
                cleaned_data = form.cleaned_data.copy()
                approval_date = cleaned_data.get('ApprovalDate')
                if approval_date:
                    approval_date_str = approval_date.strftime('%Y-%m-%d')
                    cleaned_data['ApprovalDate'] = approval_date_str
                # Sérialisation des données en JSON
                data_input = json.dumps(cleaned_data)
                with Session() as session:
                    response = session.post(api_url, data=data_input, headers=headers)
                    data = response.json()
                form.save()
                return render(request, "main/formulaire.html", context = {"formulaire": form, 'data': data})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError, JSONDecodeError) as e:
                return render(request, "main/formulaire.html", context = {"formulaire": form, 'error': e})
        else:
            # Ici, vous devriez retourner le formulaire invalide avec les erreurs
            return render(request, "main/formulaire.html", context = {"formulaire": form})
    else:
        # Ici, vous devriez retourner un formulaire vide pour une requête GET
        form = ModelApiForm()
        return render(request, "main/formulaire.html", context = {"formulaire": form})
    

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'main/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Rediriger l'utilisateur vers la page de connexion après inscription
        else:
            # Si le formulaire n'est pas valide, afficher à nouveau le formulaire avec les erreurs
            return render(request, 'main/register.html', {'form': form})
        

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back !')
                return redirect('home')
        
        # form is not valid or user is not authenticated
            messages.error(request,f'Invalid username or password')
            return render(request, 'main/login.html', {'form': form})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))