from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login, logout



# ================== Home ============================


class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Bienvenue sur  L'API ACEDH!"})

# ================= Insert user ===================================


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

# ================ Connexion Login ===================================


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request):
        user = request.user  # utilisateur connecté

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response(
                {"error": "Ancien mot de passe incorrect"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Mot de passe modifié avec succès"},
            status=status.HTTP_200_OK
        )

# ================ Connexion Login ===================================

class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)

            return Response({
                "message": "Connexion réussie"
            })
        else:
            return Response(
                {"error": "Email ou mot de passe incorrect"},
                status=status.HTTP_401_UNAUTHORIZED
            )  

class LogoutView(APIView):
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"Msg": "Successfully logged out."}, status=status.HTTP_200_OK)
    

# ======================== Fin  =================================

# ======================== Team  =================================

class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamUpdateView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

class TeamDeleteView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

# ======================== Partenaire  =================================


class PartenaireCreateView(generics.CreateAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer


class PartenaireListView(generics.ListAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer

class PartenaireUpdateView(generics.UpdateAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    lookup_field = 'id'

class PartenaireDeleteView(generics.DestroyAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    lookup_field = 'id'
