from django import forms
from django.forms.extras.widgets import *

class InscriptionForm(forms.Form):
    prenom = forms.CharField(label="Prénom", max_length=30, widget=forms.TextInput())
    nom = forms.CharField(label="Nom", max_length=30, widget=forms.TextInput())
    modeleCompte = forms.ChoiceField(label='Type de compte', choices=(
        ("professeur", "Professeur"),
        ("etudiant", "Étudiant"),
        ))
    pseudo = forms.CharField(label="Pseudo", max_length=30, widget=forms.TextInput())
    motDePasse = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())

class ConnexionForm(forms.Form):
    pseudo = 
    motDePasse = 
    
class CreerClasseForm(forms.Form):
    nom =
    branche =
    
class EtudiantAjoutForm(forms.Form):
    etudiants =

class EtudiantSupprForm(forms.Form):
    etudiants =

class CreerDevoirForm(forms.Form):
    titre =
    consigne =
    consigneImg =
    reponse =
    reponseImg =
    dateReddition =
    classe =
    
class DevoirConsImgForm(forms.Form):
    consigneImg =

class DevoirRepForm(forms.Form):
    reponse =

class DevoirRepImgForm(forms.Form):
    reponseImg =

class DevoirDateForm(forms.Form):
    dateReddition =

class ChargerImageForm(forms.Form):
    photo =
    description =