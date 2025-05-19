from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('service/', views.service, name='service'),
    path('partenaire/', views.partenaire, name='partenaire'),
    path('propos/', views.propos, name='propos'),
    path('faq/', views.faq, name='faq'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('contact/', views.contact, name='contact'),
    path('auth/', views.auth, name='auth'),
    path('politique_confidentialite/', views.politique_confidentialite, name='politique_confidentialite'),
    path('conditions_utilisation/', views.conditions_utilisation, name='conditions_utilisation'),
    path('support_contact/', views.support_contact, name='support_contact'),


    # Routes pour l'application crypto
    path('dashboard/', views.dashboard, name='dashboard'),
    path('market/', views.market, name='market'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('transactions/', views.transactions, name='transactions'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),

]