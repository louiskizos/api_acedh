from django.contrib.auth.models import User
from django.db import models






class Team(models.Model):
    
    image = models.ImageField(upload_to='images/')
    noms = models.TextField()
    fonction = models.TextField()

    def __str__(self):
        return self.noms
    


class Contact(models.Model):
    telephone = models.CharField(max_length=100)
    message = models.TextField( default='Non renseigné')
    
    def __str__(self):
        return self.telephone
    

class Adresse(models.Model):
    adresse = models.TextField()
    
    def __str__(self):
        return self.adresse


class Ressource(models.Model):
    titre = models.CharField(max_length=255)
    fichier_pdf = models.FileField(upload_to='pdfs/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    

class Mail_liste(models.Model):
    prenom = models.TextField()
    noms = models.TextField()
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.mail



class Aprops(models.Model):
    element_1 = models.TextField()
    element_2 = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.element_1
  


class Objectif(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    def __str__(self):
        return self.titre
    


class Projet(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_debit = models.DateField()
    date_fin = models.DateField()
    def __str__(self):
        return self.titre
    
class Rapport(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE,)
    commentaire = models.TextField(default='Non renseigné')
    fichier_pdf = models.FileField(upload_to='rapports/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    

class Statistique(models.Model):

    titre = models.TextField()
    estimation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titre



class Partenaire(models.Model):
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.logo.url
    


class Accompagnement(models.Model):
    titre = models.TextField()
    resume = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titre
  



class Environnement(models.Model):
    titre = models.TextField()
    resume = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titre
 


class Gallerie(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, default=None)
    detail_activite = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.detail_activite
 
class Activite(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()    
    photo = models.ImageField(upload_to='images/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre



class Commentaire(models.Model):
    article = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='commentaires')
    nom = models.CharField(max_length=100)
    contenu = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)
    approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"Commentaire de {self.nom}"