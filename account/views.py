from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User
from .serializers import DeckSerializer, UserSerializer
import re


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data
            first_name = data["first_name"]
            last_name = data["last_name"]
            username = data["username"]
            email = data["email"]
            password = data["password"]
            re_password = data["re_password"]

            emailRegex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            # CHEQUEAMOS SI SE PUEDE CREAR EL USUARIO
            if password != re_password:
                return Response(
                    {"error": "Las constrseñas no coinciden"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if len(password) < 8:
                return Response(
                    {"error": "La contraseña debe contener al menos 8 digitos"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not re.search(emailRegex, email):
                return Response(
                    {"error": "No es un email"}, status=status.HTTP_400_BAD_REQUEST
                )
            if (
                User.objects.filter(username=username).exists()
                or User.objects.filter(email=email).exists()
            ):
                return Response(
                    {"error": "El usuario ya existe"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            # SE CREA EL USUARIO
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )

            user.save()

            # ULTIMA VERIFICACION
            if User.objects.filter(username=username).exists():
                return Response(
                    {"success": "Usuario creado satisfactoriamente"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "Algo salio mal al crear al usuario"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except:
            return Response(
                {"error": "Algo salio mal al cargar al usuario"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LoadUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            print(user.data)

            return Response({"user": user.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Algo salio mal al cargar al usuario"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
