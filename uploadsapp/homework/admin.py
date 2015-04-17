from django.contrib import admin
from homework.models import Etudiant, Professeur, Classe, Image, Devoir

admin.site.register(Etudiant)
admin.site.register(Professeur)
admin.site.register(Classe)
admin.site.register(Image)
admin.site.register(Devoir)