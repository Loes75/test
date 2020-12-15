from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import UsuarioSerializer
from .models import Usuario
from .services import get_coordinates
from rest_framework.renderers import TemplateHTMLRenderer

class UsuarioCreate(generics.CreateAPIView):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class UsuarioList(generics.ListAPIView):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class UsuarioDelete(generics.DestroyAPIView):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class UsuarioGeoCode(generics.ListAPIView):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

    def get_queryset(self):
        usersWithoutGeo =Usuario.objects.filter(latitud = None)
        for user in usersWithoutGeo:
            result = get_coordinates(user.direccion,user.ciudad)
            if(result != 0):
                user.latitud=result[0]
                user.longitud=result[1]
                user.estadogeo=result[2]
                user.save()
            else:
                user.latitud=0
                user.longitud=0
            
        return usersWithoutGeo
