from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate

from django.db import IntegrityError

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')
        except IntegrityError:  # Importez cette exception si ce n'est pas déjà fait
            error_message = "Votre compte existe déjà. Veuillez choisir un autre nom d'utilisateur."
            return render(request, 'accounts/signup.html', {'error_message': error_message})

    return render(request, 'accounts/signup.html')



def logout_user(request):
    logout(request)
    return redirect('index')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')  # Redirection vers la page d'accueil après connexion réussie
        else:
            # Gérer le cas où l'authentification échoue (par exemple, afficher un message d'erreur)
            return render(request, 'accounts/login.html', {'error_message': 'Identifiants invalides'})

    # Si la méthode de requête est GET, afficher simplement le formulaire de connexion
    return render(request, 'accounts/login.html')

