from django.urls import path
from .views import UsuarioCreate,UsuarioList,UsuarioUpdate,UsuarioDelete,UsuarioGeoCode

urlpatterns=[
    path('crear',UsuarioCreate.as_view()),
    path('lista',UsuarioList.as_view()),
    path('usuario/<int:pk>',UsuarioUpdate.as_view()),
    path('eliminar/<int:pk>',UsuarioDelete.as_view()),
    path('geocodificar_base',UsuarioGeoCode.as_view()),
]