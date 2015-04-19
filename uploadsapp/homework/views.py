from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from homework.auth_utils import *
from homework.forms import *
from homework.models import *

def accueil(request):
    return render(request, "homework/accueil.html")
    
def inscription(request):
    if request.method == "POST":
        inscriptionform = InscriptionForm(data=request.POST)
        
        if inscriptionform.is_valid():
            username = inscriptionform.cleaned_data["pseudo"]
            password = inscriptionform.cleaned_data["motDePasse"]
            first_name = inscriptionform.cleaned_data["Prénom"]
            last_name = inscriptionform.cleaned_data["Nom"]
            
            try:
                User.objects.get(username=username)
            
            except User.DoesNotExist:
                modeleCompte = None
                
                if inscriptionform.cleaned_data["modèleCompte"] == "etudiant":
                    modeleCompte = Etudiant
                    group_name = "étudiants"
                    
                elif inscriptionform.cleaned_data["modèleCompte"] == "professeur":
                    modeleCompte = Professeur
                    group_name = "professeurs"
                    
                user = User.objects.create_user(username, password, first_name, last_name)
                
                try:
                    group = Group.objects.get(name=group_name)
                
                except:
                    group = Group.objects.create(name=group_name)
                
                user.groups.add(group)
                user.save()
                    
                compte = modeleCompte() 
                compte.user = user
                compte.save()
                
                return redirect('uploads:connexion')

    else:
        inscriptionform = InscriptionForm()
        
    return render(request, "homework/inscription.html", locals())