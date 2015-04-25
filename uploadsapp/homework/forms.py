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
    pseudo = forms.CharField(label="Pseudo", max_length=30, widget=forms.TextInput())
    motDePasse = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())
    
class CreerClasseForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=50, widget=forms.TextInput())
    branche = forms.ChoiceField(label='Branche', choices=(
        ("", "Choisissez votre Branche"),
        ("Allemand", "Allemand"),
        ("Anglais", "Anglais"),
        ("Arts Visuels", "Arts Visuels"),
        ("Biologie", "Biologie"),
        ("Chimie", "Chimie"),
        ("Français", "Français"),
        ("Histoire", "Histoire"),
        ("Maths", "Maths"),
        ("Musique", "Musique"),
        ("Philosophie", "Philosophie"),
        ("Physique", "Physique"),
        ("Sport", "Sport"),
        ))
    
class EtudiantAjoutForm(forms.Form):
    etudiants = forms.ModelMultipleChoiceField(label="Etudiants à ajouter", queryset=Classe.objects.all(), to_field_name="user.username", widget=forms.CheckboxSelectMultiple())
    classes = forms.ModelMultipleChoiceField(label="", queryset=Classe.objects.all(), to_field_name="", widget=forms.CheckboxSelectMultiple())
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