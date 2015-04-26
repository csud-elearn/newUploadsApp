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

class EtudiantSupprForm(forms.Form):
    etudiants = forms.ModelMultipleChoiceField(label="Etudiants à supprimer", queryset=Classe.objects.all(), to_field_name="user.username", widget=forms.CheckboxSelectMultiple())

class CreerDevoirForm(forms.Form):
    titre = forms.CharField(label="Titre", max_length=50, widget=forms.TextInput())
    consigne = forms.CharField(label="Consigne", max_length=300, widget=forms.Textarea())
    consigneImg = forms.ImageField(label="Consigne en image", required=False, widget=forms.FileInput())
    reponse = forms.CharField(label="Réponse", required=False, max_length=300, widget=forms.Textarea())
    reponseImg = forms.ImageField(label="Réponse en image", required=False, widget=forms.FileInput())
    dateReddition = forms.DateField(label="Date de reddition", widget=formsDatePicker())
    classe = forms.ModelMultipleChoiceField(label="Classes", queryset=Classe.objects.all(), to_field_name="nom", widget=forms.CheckboxSelectMultiple())
    
class DevoirConsImgForm(forms.Form):
    consigneImg = forms.ImageField(label="Consigne en image", widget=forms.FileInput())

class DevoirRepForm(forms.Form):
    reponse = forms.CharField(label="Réponse", max_length=300, widget=forms.Textarea())

class DevoirRepImgForm(forms.Form):
    reponseImg = forms.ImageField(label="Réponse en image", widget=forms.FileInput())

class DevoirDateForm(forms.Form):
    dateReddition = forms.DateField(label="Date de reddition", widget=formsDatePicker())

class ChargerImageForm(forms.Form):
    photo = forms.ImageField(label="Photo", widget=forms.FileInput())
    description = forms.CharField(label="Consigne", required=False, max_length=300, widget=forms.Textarea())