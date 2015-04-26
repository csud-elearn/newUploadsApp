from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from homework.auth_utils import *
from homework.models import *
from homework.forms import *

def accueil(request):
    return render(request, "homework/accueil.html")
    
def inscription(request):
    if request.method == "POST":
        inscriptionform = InscriptionForm(request.POST, request.FILES)
        
        if inscriptionform.is_valid():
            username = inscriptionform.cleaned_data["pseudo"]
            password = inscriptionform.cleaned_data["motDePasse"]
            first_name = inscriptionform.cleaned_data["prenom"]
            last_name = inscriptionform.cleaned_data["nom"]
            
            try:
                User.objects.get(username=username)
            
            except User.DoesNotExist:
                modeleCompte = None
                
                if inscriptionform.cleaned_data["modeleCompte"] == "etudiant":
                    modeleCompte = Etudiant()
                    group_name = "étudiants"
                    
                elif inscriptionform.cleaned_data["modeleCompte"] == "professeur":
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
    
    if request.user.is_authenticated():
        return render(request, "homework/connexionConnecte.html", locals())
    else:    
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
            
        return render(request, "homework/connexionDeconnecte.html", locals())
    
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
            creerClasseForm = CreerClasseForm(request.POST, request.FILES)
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
        classes = etudiant.classe.all()
        
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
                if request.method == "POST":
                    if 'etudiantSuppr' in request.POST:
                        etudiantSupprForm = EtudiantSupprForm(request.POST, request.FILES)              #<form action="" method="post">
                        if etudiantSupprForm.is_valid():                                                #{{ form_newsletter }}
                            for etudiant in etudiantSupprForm.cleaned_data["etudiants"]:                #<input type="submit" name="newsletter_sub" value="Subscribe" />
                                etudiant.classe.add(classe)                                             #<input type="submit" name="newsletter_unsub" value="Unsubscribe" />
                                etudiant.save()                                                         #</form>
        
                    elif 'etudiantAjout' in request.POST:
                        etudiantAjoutForm = EtudiantAjoutForm(request.POST, request.FILES)
                        if etudiantAjoutForm.is_valid():
                            for etudiant in etudiantAjoutForm.cleaned_data["etudiants"]:
                                etudiant.classe.add(classe)
                                etudiant.save()
                
                else:
                    etudiantSupprForm = EtudiantSupprForm()
                    etudiantAjoutForm = EtudiantAjoutForm()
                
                etudiantSupprForm.fields['etudiants'].queryset = Etudiant.objects.filter(classe=classe)
                etudiantAjoutForm.fields['etudiants'].queryset = Etudiant.objects.exclude(classe=classe)
                
                return render(request, "professeur/classeEditionPropre.html", locals())
            else:
                return render(request, "professeur/classeEditionAutre.html", locals())
        
        elif estEtudiant(request.user):
            etudiantConnecte = Etudiant.objects.get(user=request.user)
            
            return render(request, "etudiant/classeEdition.html", locals())
    
    else:
        return redirect("homework:connexion")

def devoirIndex(request):
    if estProfesseur(request.user):
        erreur = False
        professeur = Professeur.objects.get(user=request.user)
        classes = Classe.objects.filter(professeur=professeur)
        devoirs = Devoir.objects.filter(professeur=professeur)
        
        if request.method == "POST":
            creerDevoirForm = CreerDevoirForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    devoir = Devoir.objects.get(titre=creerDevoirForm.cleaned_data["titre"])
                    erreur = True
                except:
                    professeur = Professeur.objects.get(user=request.user)
                    devoir = Devoir()
                    devoir.titre = creerDevoirForm.cleaned_data["titre"]
                    devoir.consigne = creerDevoirForm.cleaned_data["consigne"]
                    devoir.consigneImg = creerDevoirForm.cleaned_data["consigneImg"]
                    devoir.reponse = creerDevoirForm.cleaned_data["reponse"]
                    devoir.reponseImg = creerDevoirForm.cleaned_data["reponseImg"]
                    devoir.dateReddition = creerDevoirForm.cleaned_data["dateReddition"]
                    devoir.save()
                    for classeNom in form.cleaned_data['classe']:
                        classe = Classe.objects.get(nom=classeNom)
                        devoir.classe.add(classe)
                        tag.save()
        else:
            creerDevoirForm = CreerDevoirForm()
        
        creerDevoirForm.fields['classe'].queryset = Classe.objects.filter(professeur=professeur)
        
        return render(request, "professeur/devoirIndex.html", locals())
    
    elif estEtudiant(request.user):
        etudiant = Etudiant.objects.get(user=request.user)
        classes = etudiant.classe.all()
        devoirs = []
        for classe in classes:
            devoirs.append(Devoir.objects.filter(classes=classe))
            #devoirs += Devoir.objects.filter(classes=classe)
        
        return render(request, "etudiant/devoirIndex.html", locals())
    
    else:
        return redirect("homework:connexion")

def devoirEdition(request, devoirTitre):
    devoir = Devoir.objects.get(titre=devoirTitre)
    if estProfesseur(request.user):
        professeurConnecte = Professeur.objects.get(user=request.user)
        devoirProfesseur = devoir.Professeur
        if professeurConnecte == devoirProfesseur:
            if request.method == "POST":
                if 'devoirConsImg' in request.POST:
                    devoirConsImgForm = DevoirConsImgForm(request.POST, request.FILES)
                    devoir.consigneImg = devoirConsImgForm.cleaned_data["consigneImg"]
                    devoir.save()
                elif 'devoirRep' in request.POST:
                    devoirRepForm = DevoirRepForm(request.POST, request.FILES)
                    devoir.reponse = devoirRepForm.cleaned_data["reponse"]
                    devoir.save()        
                elif 'devoirRepImg' in request.POST:
                    devoirRepImgForm = DevoirRepImgForm(request.POST, request.FILES)
                    devoir.reponseImg = devoirRepImgForm.cleaned_data["reponseImg"]
                    devoir.save()    
                elif 'devoirDate' in request.POST:
                    devoirDateForm = DevoirDateForm(request.POST, request.FILES)
                    devoir.dateReddition = devoirDateForm.cleaned_data["dateReddition"]
                    devoir.save()
            else:
                devoirConsImgForm = DevoirConsImgForm()
                devoirRepForm = DevoirRepForm()
                devoirRepImgForm = DevoirRepImgForm()
                devoirDateForm = DevoirDateForm()
            
            return render(request, "professeur/devoirEditionPropre.html", locals())
        else:
            return render(request, "professeur/devoirEditionAutre.html", locals()) 
    elif estEtudiant(request.user):
        etudiant = Etudiant.objects.get(user=request.user)
        autorise = False
        for devoirClasse in devoir.classe:
            if devoirClasse in etudiant.classe:
                autorise = True
        if autorise:
            return render(request, "etudiant/devoirEditionPropre.html", locals())
        else:
            return render(request, "etudiant/devoirEditionAutre.html", locals())
    else:
        return redirect("homework:connexion")

def chargerImage(request, devoirTitre):
    if estProfesseur(request.user):
        return render(request, "professeur/nonAutorise.html", locals())
    
    elif estEtudiant(request.user):
        devoir = Devoir.objects.get(titre=devoirTitre)
        etudiant = Etudiant.objects.get(user=request.user)
        if request.method == "POST":
            chargerImageForm = ChargerImageForm(request.POST, request.FILES)
            if chargerImageForm.is_valid():
                image = Image()
                image.etudiant = etudiant
                image.photo = chargerImageForm.cleaned_data["photo"]
                image.devoir = devoir
                image.description = chargerImageForm.cleaned_data["description"]
        else:
            chargerImageForm = ChargerImageForm()
        
        return render(request, "etudiant/chargerImage.html", locals())
    else:
        return redirect("homework:connexion")

def imageIndexEtudiant(request):
    if estProfesseur(request.user):
        return render(request, "professeur/nonAutorise.html", locals())
    elif estEtudiant(request.user):
        etudiant = Etudiant.objects.get(user=request.user)
        imageAucune = False
        try:
            images = Image.objects.filter(etudiant=etudiant)
        except:
            imageAucune = True
            
        return render(request, "etudiant/imageIndex.html", locals())
    else:
        return redirect("homework:connexion")

def imageEditionEtudiant(request, devoirTitre):
    if estProfesseur(request.user):
        return render(request, "professeur/nonAutorise.html", locals())
    elif estEtudiant(request.user):
        etudiant = Etudiant.objects.get(user=request.user)
        imageAucune = False
        try:
            devoir = Devoir.objects.get(titre=devoirTitre)
            images = Image.objects.filter(etudiant=etudiant)
            image = images.objects.get(devoir=devoir)
        except:
            imageAucune = True
        
        return render(request, "etudiant/imageEdition.html", locals())
    else:
        return redirect("homework:connexion")

def imageIndexProfesseur(request, devoirTitre, classeNom):
    if estEtudiant(request.user):
        return render(request, "etudiant/nonAutorise.html", locals())
    elif estProfesseur(request.user):
        professeur = Professeur.objects.get(user=request.user)
        devoir = Devoir.objects.get(titre=devoirTitre)
        if devoir.professeur == professeur:
            classe = Classe.objects.get(nom=classeNom)
            etudiants = Etudiant.objects.filter(classe=classe)
            images = Image.objects.filter(devoir=devoir, [etudiant=etudiant for etudiant in etudiants])
            #imagesDevoirClasse = imagesDevoir.filter(etudiant in etudiants)
            #imagesDevoirClasse = []
            #for etudiant in etudiants:
            #try:
            #   image = imagesDevoir.get(etudiant=etudiant)
            #   imagesDevoirClasse.append(image)
            #except:
            #   pass
            return render(request, "professeur/imageIndex.html", locals())
        else:
            return render(request, "professeur/nonAutorise.html", locals())
    else:
        return redirect("homework:connexion")

def imageEditionProfesseur(request, devoirTitre, etudiantUsername):
    if estEtudiant(request.user):
        return render(request, "etudiant/nonAutorise.html", locals())
    elif estProfesseur(request.user):
        devoir = Devoir.objects.get(titre=devoirTitre)
        professeur = Professeur.objects.get(request.user)
        if professeur == devoir.professeur:
            etudiant = Etudiant.objects.get(user.username=etudiantUsername)
            imageEleve = Image.objects.filter(etudiant=etudiant, devoir=devoir)
                
            return render(request, "professeur/imageEdition.html", locals())
        else:
            return render(request, "professeur/nonAutorise.html", locals())
    else:
        return redirect("homework:connexion")