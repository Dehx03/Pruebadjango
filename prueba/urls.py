
from django.contrib import admin
from django.urls import path
from users import views

from users.views import Registro,Login
urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/register/', Registro.as_view(), name='register'),
     path('api/login/', Login.as_view(), name='login'),
     path('obtener/', views.obtener_datos_usuario, name='obtener_datos_usuario'),
]
