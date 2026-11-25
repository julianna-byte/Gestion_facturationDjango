from django.urls import path

from . import views

urlpatterns = [
    # Gestion des clients
    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),

    # Gestion des produits
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),

    # Gestion des factures
    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/ajouter/', views.ajouter_facture, name='ajouter_facture'),
    path(
        'factures/<int:facture_id>/',
        views.detail_facture,
        name='detail_facture',
    ),
    path(
        'factures/<int:facture_id>/ajouter-ligne/',
        views.ajouter_ligne,
        name='ajouter_ligne',
    ),
    path(
        'factures/<int:facture_id>/ajouter-paiement/',
        views.ajouter_paiement,
        name='ajouter_paiement',
    ),
]