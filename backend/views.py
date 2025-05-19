from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Crypto

# Create your views here.

def acceuil(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def connexion(request):
    return render(request, 'connexion.html')

def inscription(request):
    return render(request, 'inscription.html')

def service(request):
    return render(request, 'service.html')

def partenaire(request):
    return render(request, 'partenaire.html')

def propos(request):
    return render(request, 'propos.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

def auth(request):
    return render(request, 'auth.html')

def politique_confidentialite(request):
    return render(request, 'politique_confidentialite.html')

def conditions_utilisation(request):
    return render(request, 'conditions_utilisation.html')

def support_contact(request):
    return render(request, 'support_contact.html')

def market(request):
    cryptos = Crypto.objects.all()
    return render(request, 'market.html', {'cryptos': cryptos})

def dashboard(request):
    return render(request, 'dashboard.html')


def buy(request):
    return render(request, 'buy.html')

def sell(request):
    return render(request, 'sell.html')

def transactions(request):
    return render(request, 'transactions.html')

def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('connexion')  # Redirige vers la page de connexion après déconnexion
