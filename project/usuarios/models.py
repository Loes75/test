from django.db import models
from django.core.validators import RegexValidator

class Usuario(models.Model):
    nombre=models.CharField(max_length=30,blank=False,validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',('Ingresa unicamente letras'))])
    apellido=models.CharField(max_length=40,blank=False,validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',('Ingresa unicamente letras'))])
    ciudad=models.CharField(max_length=40,blank=False,validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',('Ingresa unicamente letras'))])
    direccion=models.CharField(max_length=100,blank=False)
    estadogeo=models.JSONField(blank=True,null=True)
    longitud=models.FloatField(blank=True,null=True)
    latitud=models.FloatField(blank=True,null=True)
    createdAt=models.DateTimeField(auto_now=True)
   
