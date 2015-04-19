from django.db import models
from django.contrib.auth.models import User


class Etudiant(models.Model):
    user = models.OneToOneField(User)
    
    def __str__(self):
        return "Etudiant {}".format(self.user.username)

class Professeur(models.Model):
    user = models.OneToOneField(User) 
    
    def __str__(self):
        return "Professeur {}".format(self.user.username)
        
class Classe(models.Model):
    nom = models.CharField(max_length=50)
    branche = models.CharField(max_length=50)
    professeur = models.ForeignKey("Professeur")
    
    def __str__(self):
        return self.nom
        
class Image(models.Model):
    etudiant = models.ForeignKey("Etudiant")
    photo = models.ImageField(upload_to="etudiants/images")
    devoir = models.ForeignKey("Devoir")
    
    description = models.CharField(max_length=300, null=True)
    
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "{}: {}".format(self.devoir, self.etudiant)
        
class Devoir(models.Model):
    professeur = models.ForeignKey("Professeur")
    classe = models.ManyToManyField("Classe")
    
    titre = models.CharField(max_length=50)
    consigne = models.CharField(max_length=300)
    consigneImg = models.ImageField(upload_to="professeur/consignes", null=True)
    reponse = models.CharField(max_length=300)
    reponseImg = models.ImageField(upload_to="professeur/corriges", null=True)
    
    dateCreation = models.DateField(auto_now_add=True)
    dateReddition = models.DateField()
    
    def __str__(self):
        return self.titre   