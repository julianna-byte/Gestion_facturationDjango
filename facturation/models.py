from decimal import Decimal

from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Facture(models.Model):
    STATUTS = [
        ('BROUILLON', 'Brouillon'),
        ('VALIDEE', 'Validée'),
        ('PAYEE', 'Payée'),
        ('ANNULEE', 'Annulée'),
    ]

    numero = models.CharField(max_length=30, unique=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='factures',
    )
    date_creation = models.DateField(auto_now_add=True)
    date_echeance = models.DateField()
    taux_tva = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('18.00'),
    )
    # Ce champ manquait dans le cours, alors que les templates utilisent
    # facture.get_statut_display
    statut = models.CharField(
        max_length=20,
        choices=STATUTS,
        default='BROUILLON',
    )

    @property
    def total_ht(self):
        return sum(
            (ligne.montant_ht for ligne in self.lignes.all()),
            Decimal('0'),
        )

    @property
    def montant_tva(self):
        return self.total_ht * self.taux_tva / Decimal('100')

    @property
    def total_ttc(self):
        return self.total_ht + self.montant_tva

    @property
    def total_paye(self):
        return sum(
            (p.montant for p in self.paiements.all()),
            Decimal('0'),
        )

    @property
    def reste_a_payer(self):
        return self.total_ttc - self.total_paye

    def __str__(self):
        return self.numero


class LigneFacture(models.Model):
    facture = models.ForeignKey(
        Facture,
        on_delete=models.CASCADE,
        related_name='lignes',
    )
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def montant_ht(self):
        return self.quantite * self.prix_unitaire

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite}"


class Paiement(models.Model):
    MODES = [
        ('ESPECES', 'Espèces'),
        ('VIREMENT', 'Virement bancaire'),
        ('CHEQUE', 'Chèque'),
        ('MOBILE_MONEY', 'Mobile Money'),
    ]

    facture = models.ForeignKey(
        Facture,
        on_delete=models.PROTECT,
        related_name='paiements',
    )
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    mode = models.CharField(max_length=20, choices=MODES)
    date_paiement = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.facture.numero} - {self.montant}"