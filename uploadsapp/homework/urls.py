from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from homework import views

urlpatterns = patterns('',

 url(r'^$', views.accueil, name='accueil'),
 url(r'^inscription/', views.inscription, name='inscription'),
 url(r'^connexion/', views.connexion, name='connexion'),
 url(r'^deconnexion', views.deconnexion, name='deconnexion'),
 url(r'^bureau', views.bureau, name='bureau'),
 url(r'^classes', views.classeIndex, name='classeIndex'),
 url(r'^classe/(?P<classeNom>\w+)', views.classeEdition, name='classeEdition'),
 url(r'^devoirs', views.devoirIndex, name='devoirIndex'),
 url(r'^devoir/(?P<devoirTitre>\w+)', name='devoirEdition')
)