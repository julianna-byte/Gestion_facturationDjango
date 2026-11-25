from django import forms

from .models import Client, Produit, Facture, LigneFacture, Paiement


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email', 'telephone', 'adresse']


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'stock']


class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'client', 'date_echeance', 'taux_tva']
        widgets = {
            'date_echeance': forms.DateInput(attrs={'type': 'date'}),
        }


class LigneFactureForm(forms.ModelForm):
    # prix_unitaire et facture sont renseignés dans la vue
    class Meta:
        model = LigneFacture
        fields = ['produit', 'quantite']


class PaiementForm(forms.ModelForm):
    # facture est renseignée dans la vue
    class Meta:
        model = Paiement
        fields = ['montant', 'mode', 'reference']