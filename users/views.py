from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, Registro
from django.http import JsonResponse
from django.contrib.auth.models import User


class Registro(generics.GenericAPIView):
    serializer_class = Registro

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
    
class Login(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(Login, self).post(request, format=None)
    
def obtener_datos_usuario(request):
    username=request.GET.get('username')
    try:
        usuario = User.objects.get(username=username)

        # Accede a los datos del usuario
        username = usuario.username
        email = usuario.email
        password = usuario.password
        last_name = usuario.last_name

        # Construye la respuesta JSON con los datos del usuario
        datos_usuario = {
            'username': username,
            'email': email,
            'password': password,
            'last_name': last_name,
        }

        return JsonResponse(datos_usuario)
    except User.DoesNotExist:
        # El usuario no existe, maneja el error adecuadamente
        return JsonResponse({'error': 'El usuario no existe.'}, status=404)