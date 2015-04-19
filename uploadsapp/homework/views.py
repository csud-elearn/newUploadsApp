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
        inscriptionform = InscriptionForm(request.POST, request.FILES)
        
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
                    modeleCompte = Etudiant()
                    group_name = "étudiants"
                    
                elif inscriptionform.cleaned_data["modèleCompte"] == "professeur":
                    modeleCompte = Professeur()
                    group_name = "professeurs"
                    
                user = User.objects.create_user(username, password, first_name, last_name)
                
                try:
                    groupe = Group.objects.get(name=group_name)
                
                except:
                    groupe = Group.objects.create(name=group_name)
                
                user.groups.add(groupe)
                user.save()
                    
                compte = modeleCompte
                compte.user = user
                compte.save()
                
                return redirect("homework:connexion")

    else:
        inscriptionform = InscriptionForm()
        
    return render(request, "homework/inscription.html", locals())

def connexion(request):
    erreur = False
    
    if request.method == "POST":
        connexionForm = ConnexionForm(request.POST, request.FILES)
        
        if connexionForm.is_valid():
            username = connexionForm.cleaned_data["pseudo"]
            password = connexionForm.cleaned_data["motDePasse"]
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                
                return redirect("homework:bureau")
            else:
                erreur = True
    else:
        connexionForm = ConnexionForm()
        
    return render(request, "homework/login.html", locals())
    
def deconnexion(request):
    logout(request)
    
    return redirect("homework:connexion")
    
def bureau(request):
    if estEtudiant(request.user):
        return render(request, "etudiant/bureau.html", locals())
    
    elif estProfesseur(request.user):
        return render(request, "professeur/bureau.html", locals())
    
    else:
        return redirect("homework:connexion")
        
def classeIndex(request):
    if estProfesseur(request.user):
        erreur = False
        professeur = Professeur.objects.get(user=request.user)
        classes = Classe.objects.filter(professeur=professeur)
        
        if request.method == "POST":
            creerClasseForm = creerClasseForm(request.POST, request.FILES)
            if creerClasseForm.is_valid():
                classeNom = creerClasseForm.cleaned_data["nom"]
                try:
                    classe = Classe.objects.get(nom=classeNom)
                    erreur = True
                except:
                    classe = Classe()
                    classe.nom = classeNom
                    classe.branche = creerClasseForm.cleaned_data["branche"]
                    classe.professeur = professeur
                    classe.save()
        else:
            creerClasseForm = creerClasseForm()
        
        return render(request, "professeur/classeIndex.html", locals())
    
    elif estEtudiant(request.user):
        etudiant = Etudiant.objects.get(user=request.user)
        classes = etudiant.classes.all()
        
        return render(request, "etudiant/classeIndex.html", locals())
        
    else:
        return redirect("homework:connexion")
        
def classeEdition(request, classeNom):
    if estProfesseur(request.user) or estEtudiant(request.user):
        classe = Classe.objects.get(nom=classeNom)
        classeEtudiants = Etudiant.objects.filter(classe=classe).order_by("user.first_name")
        classeProfesseur = classe.professeur
        etudiantsTous = Etudiant.objects.exclude(classe=classe)
        
        if estProfesseur(request.user):
            professeurConnecte = Professeur.objects.get(user=request.user)
            if professeurConnecte == classeProfesseur:
                return render(request, "professeur/classeEditionPropre.html", locals())
            else:
                return render(request, "professeur/classeEditionAutre.html", locals())
        
        elif estEtudiant(request.user):
            etudiantConnecte = Etudiant.objects.get(user=request.user)
            
            return render(request, "etudiant/classeEdition.html", locals())
    
    else:
        return redirect("homework:connexion")
        
    
    