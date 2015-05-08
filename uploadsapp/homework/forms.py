from django import forms
from django.forms.extras.widgets import *

from homework.models import Classe, Etudiant

class InscriptionForm(forms.Form):
    prenom = forms.CharField(label="Prénom", max_length=30, widget=forms.TextInput(attrs={'class': 'validate', 'type': 'text'}))
    nom = forms.CharField(label="Nom", max_length=30, widget=forms.TextInput(attrs={'class': 'validate', 'type': 'text'}))
    courriel = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'validate', 'type': 'email'}))
    modeleCompte = forms.ChoiceField(label='Type de compte', choices=(
        ("professeur", "Professeur"),
        ("etudiant", "Étudiant"),
        ))
    pseudo = forms.CharField(label="Pseudo", max_length=30, widget=forms.TextInput(attrs={'class': 'validate', 'type': 'text'}))
    motDePasse = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'validate', 'type': 'password'}))

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
    etudiants = forms.ModelMultipleChoiceField(label="Etudiants à ajouter", queryset=Etudiant.objects.all(), to_field_name="id", widget=forms.CheckboxSelectMultiple())

class EtudiantSupprForm(forms.Form):
    etudiants = forms.ModelMultipleChoiceField(label="Etudiants à supprimer", queryset=Etudiant.objects.all(), to_field_name="id", widget=forms.CheckboxSelectMultiple())

class QuitterClasseForm(forms.Form):
    nomClasse = forms.CharField(label="Saisir le nom de la classe pour quitter", max_length=50, widget=forms.TextInput())
    
class CreerDevoirForm(forms.Form):
    titre = forms.CharField(label="Titre", max_length=50, widget=forms.TextInput())
    consigne = forms.CharField(label="Consigne", max_length=300, widget=forms.Textarea())
    consigneImg = forms.ImageField(label="Consigne en image", widget=forms.FileInput(attrs={'accept': 'image/*'}))
    reponse = forms.CharField(label="Réponse",  max_length=300, widget=forms.Textarea())
    reponseImg = forms.ImageField(label="Réponse en image", widget=forms.FileInput(attrs={'accept': 'image/*'}))
    dateReddition = forms.DateField(label="Date de reddition", widget=forms.DateInput())
    classe = forms.ModelMultipleChoiceField(label="Classes", queryset=Classe.objects.all(), to_field_name="id", widget=forms.CheckboxSelectMultiple())
    
class DevoirConsForm(forms.Form):
    consigne = forms.CharField(label="Consigne", max_length=300, widget=forms.Textarea())
    
class DevoirConsImgForm(forms.Form):
    consigneImg = forms.ImageField(label="Consigne en image", widget=forms.FileInput())

class DevoirRepForm(forms.Form):
    reponse = forms.CharField(label="Réponse", max_length=300, widget=forms.Textarea())

class DevoirRepImgForm(forms.Form):
    reponseImg = forms.ImageField(label="Réponse en image", widget=forms.FileInput())

class DevoirDateForm(forms.Form):
    dateReddition = forms.DateField(label="Date de reddition", widget=forms.DateInput())

class ChargerImageForm(forms.Form):
    photo = forms.ImageField(label="Photo", widget=forms.FileInput(attrs={'class': 'file-path validate', 'type': 'file'}))
    description = forms.CharField(label="Description", required=False, max_length=300, widget=forms.Textarea(attrs={'class': 'validate', 'type': 'text'}))