from django.db import models

# Create your models here.
class Department(models.Model):

    intitule=models.CharField(max_length=100)
    etage=models.IntegerField()

    def __str__(self):
        return self.intitule

class Employe(models.Model):

    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    ville =models.CharField(max_length=60)
    poste = models.CharField(max_length=60)
    salaire = models.FloatField()
    departement = models.ForeignKey(Department, related_name="employes", on_delete=models.CASCADE)
