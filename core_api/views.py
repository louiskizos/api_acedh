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

# ======================== Activite  =================================


class ActiviteCreateView(generics.CreateAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer


class ActiviteListView(generics.ListAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer

class ActiviteUpdateView(generics.UpdateAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
    lookup_field = 'id'

class ActiviteDeleteView(generics.DestroyAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
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
    


# ======================== Gallerie  =================================


class GallerieCreateView(generics.CreateAPIView):
    queryset = Gallerie.objects.all()
    serializer_class = GallerieSerializer


class GallerieListView(generics.ListAPIView):
    queryset = Gallerie.objects.all()
    serializer_class = GallerieSerializer

class GallerieUpdateView(generics.UpdateAPIView):
    queryset = Gallerie.objects.all()
    serializer_class = GallerieSerializer
    lookup_field = 'id'

class GallerieDeleteView(generics.DestroyAPIView):
    queryset = Gallerie.objects.all()
    serializer_class = GallerieSerializer
    lookup_field = 'id'
    


# ======================== Environnement  =================================


class EnvironnementCreateView(generics.CreateAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer


class EnvironnementListView(generics.ListAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer

class EnvironnementUpdateView(generics.UpdateAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer
    lookup_field = 'id'

class EnvironnementDeleteView(generics.DestroyAPIView):
    queryset = Environnement.objects.all()
    serializer_class = EnvironnementSerializer
    lookup_field = 'id'



# ======================== Accompagnement  =================================


class AccompagnementCreateView(generics.CreateAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer


class AccompagnementListView(generics.ListAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer

class AccompagnementUpdateView(generics.UpdateAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer
    lookup_field = 'id'

class AccompagnementDeleteView(generics.DestroyAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer
    lookup_field = 'id'
    


# ======================== Statistique  =================================


class StatistiqueCreateView(generics.CreateAPIView):
    queryset = Statistique.objects.all()
    serializer_class = StatistiqueSerializer


class StatistiqueListView(generics.ListAPIView):
    queryset = Statistique.objects.all()
    serializer_class =StatistiqueSerializer

class StatistiqueUpdateView(generics.UpdateAPIView):
    queryset = Statistique.objects.all()
    serializer_class = StatistiqueSerializer
    lookup_field = 'id'

class StatistiqueDeleteView(generics.DestroyAPIView):
    queryset = Statistique.objects.all()
    serializer_class = StatistiqueSerializer
    lookup_field = 'id'
    
# ======================== Accompagnement  =================================


class AccompagnementCreateView(generics.CreateAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer


class AccompagnementListView(generics.ListAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer

class AccompagnementUpdateView(generics.UpdateAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer
    lookup_field = 'id'

class AccompagnementDeleteView(generics.DestroyAPIView):
    queryset = Accompagnement.objects.all()
    serializer_class = AccompagnementSerializer
    lookup_field = 'id'



# ======================== Adresse  =================================


class AdresseCreateView(generics.CreateAPIView):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer


class AdresseListView(generics.ListAPIView):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer

class AdresseUpdateView(generics.UpdateAPIView):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer
    lookup_field = 'id'

class AdresseDeleteView(generics.DestroyAPIView):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer
    lookup_field = 'id'
    


# ======================== Contact  =================================


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactUpdateView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

class ContactDeleteView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'



# ======================== Ressource  =================================


class RessourceCreateView(generics.CreateAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class RessourceListView(generics.ListAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer

class RessourceUpdateView(generics.UpdateAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
    lookup_field = 'id'

class RessourceDeleteView(generics.DestroyAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
    lookup_field = 'id'
         


# ======================== Mail_liste  =================================


class Mail_listeCreateView(generics.CreateAPIView):
    queryset = Mail_liste.objects.all()
    serializer_class = Mail_listeSerializer


class Mail_listeListView(generics.ListAPIView):
    queryset = Mail_liste.objects.all()
    serializer_class = Mail_listeSerializer

class Mail_listeUpdateView(generics.UpdateAPIView):
    queryset = Mail_liste.objects.all()
    serializer_class = Mail_listeSerializer
    lookup_field = 'id'

class Mail_listeDeleteView(generics.DestroyAPIView):
    queryset = Mail_liste.objects.all()
    serializer_class = Mail_listeSerializer
    lookup_field = 'id'
         



# ======================== Apropos  =================================


class AproposCreateView(generics.CreateAPIView):
    queryset = Aprops.objects.all()
    serializer_class = AproposSerializer


class AproposListView(generics.ListAPIView):
    queryset = Aprops.objects.all()
    serializer_class = AproposSerializer

class AproposUpdateView(generics.UpdateAPIView):
    queryset = Aprops.objects.all()
    serializer_class = AproposSerializer
    lookup_field = 'id'

class AproposDeleteView(generics.DestroyAPIView):
    queryset = Aprops.objects.all()
    serializer_class = AproposSerializer
    lookup_field = 'id'
         

# ======================== Objectif  =================================


class ObjectifCreateView(generics.CreateAPIView):
    queryset = Objectif.objects.all()
    serializer_class = ObjectifSerializer


class ObjectifListView(generics.ListAPIView):
    queryset = Objectif.objects.all()
    serializer_class = ObjectifSerializer

class ObjectifUpdateView(generics.UpdateAPIView):
    queryset = Objectif.objects.all()
    serializer_class = ObjectifSerializer
    lookup_field = 'id'

class ObjectifDeleteView(generics.DestroyAPIView):
    queryset = Objectif.objects.all()
    serializer_class = ObjectifSerializer
    lookup_field = 'id'
         


# ======================== Projet  =================================


class ProjetCreateView(generics.CreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer


class ProjetListView(generics.ListAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class ProjetUpdateView(generics.UpdateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    lookup_field = 'id'

class ProjetDeleteView(generics.DestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    lookup_field = 'id'
      