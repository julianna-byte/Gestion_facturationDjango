from django.contrib import admin
from .models import (    Client,    Produit,    Facture,    LigneFacture,    Paiement)
# Enregistrement du modèleClient
admin.site.register(Client)
# Enregistrement du modèleProduit
admin.site.register(Produit)
#Enregistrement du modèleFacture
admin.site.register(Facture)
# Enregistrement du modèleLigneFacture
admin.site.register(LigneFacture)
# Enregistrement du modèlePaiement
admin.site.register(Paiement)