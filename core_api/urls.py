from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # ============ LogIn et Register ============================

    path('user/', UserListView.as_view()), 
    path('register/', RegisterView.as_view()), 
    path('login/', LoginView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view()),

    # ======================== Team  =================================

    path('team/', TeamListView.as_view()),             
    path('team/create/', TeamCreateView.as_view()),    
    path('team/<int:id>/update/', TeamUpdateView.as_view()),  
    path('team/<int:id>/delete/', TeamDeleteView.as_view()),  

    # ======================== Partenaire  =================================

    path('partenaire/', PartenaireListView.as_view()),             
    path('partenaire/create/', PartenaireCreateView.as_view()),    
    path('partenaire/<int:id>/update/', PartenaireUpdateView.as_view()),  
    path('partenaire/<int:id>/delete/', PartenaireDeleteView.as_view()),  


    # ======================== Activite  =================================

    path('activite/', ActiviteListView.as_view()),             
    path('activite/create/', ActiviteCreateView.as_view()),    
    path('activite/<int:id>/update/', ActiviteUpdateView.as_view()),  
    path('activite/<int:id>/delete/', ActiviteDeleteView.as_view()),  
    path('activite/<int:pk>/', ActiviteDetailView.as_view(), name='activite-detail'),



    # ======================== Gallerie  =================================

    path('gallerie/', GallerieListView.as_view()),             
    path('gallerie/create/', GallerieCreateView.as_view()),    
    path('gallerie/<int:id>/update/', GallerieUpdateView.as_view()),  
    path('gallerie/<int:id>/delete/', GallerieDeleteView.as_view()), 
    path('gallerie/<int:projet_id>/gallerie_projet/', GallerieByProjetView.as_view(), name='projet-gallerie'),

    
    # ======================== Environnement  =================================

    path('environnement/', EnvironnementListView.as_view()),             
    path('environnement/create/', EnvironnementCreateView.as_view()),    
    path('environnement/<int:id>/update/', EnvironnementUpdateView.as_view()),  
    path('environnement/<int:id>/delete/', EnvironnementDeleteView.as_view()),  


    # ======================== Accompagnement  =================================

    path('accompagnement/', AccompagnementListView.as_view()),             
    path('accompagnement/create/', AccompagnementCreateView.as_view()),    
    path('accompagnement/<int:id>/update/', AccompagnementUpdateView.as_view()),  
    path('accompagnement/<int:id>/delete/', AccompagnementDeleteView.as_view()),  


    # ======================== Statistique  =================================

    path('statistique/', StatistiqueListView.as_view()),             
    path('statistique/create/', StatistiqueCreateView.as_view()),    
    path('statistique/<int:id>/update/', StatistiqueUpdateView.as_view()),  
    path('statistique/<int:id>/delete/', StatistiqueDeleteView.as_view()), 



    # ======================== Adresse  =================================

    path('adresse/', AdresseListView.as_view()),             
    path('adresse/create/', AdresseCreateView.as_view()),    
    path('adresse/<int:id>/update/', AdresseUpdateView.as_view()),  
    path('adresse/<int:id>/delete/', AdresseDeleteView.as_view()), 



    # ======================== Contact  =================================

    path('contact/', ContactListView.as_view()),             
    path('contact/create/', ContactCreateView.as_view()),    
    path('contact/<int:id>/update/', ContactUpdateView.as_view()),  
    path('contact/<int:id>/delete/', ContactDeleteView.as_view()),

    # ======================== Contact  =================================

    path('contact/', ContactListView.as_view()),             
    path('contact/create/', ContactCreateView.as_view()),    
    path('contact/<int:id>/update/', ContactUpdateView.as_view()),  
    path('contact/<int:id>/delete/', ContactDeleteView.as_view()),


    # ======================== Ressource  =================================

    path('ressource/', RessourceListView.as_view()),             
    path('ressource/create/', RessourceCreateView.as_view()),    
    path('ressource/<int:id>/update/', RessourceUpdateView.as_view()),  
    path('ressource/<int:id>/delete/', RessourceDeleteView.as_view()),


    # ======================== Mail_liste  =================================

    path('mail_liste/', Mail_listeListView.as_view()),             
    path('mail_liste/create/', Mail_listeCreateView.as_view()),    
    path('mail_liste/<int:id>/update/', Mail_listeUpdateView.as_view()),  
    path('mail_liste/<int:id>/delete/', Mail_listeDeleteView.as_view()),


    # ======================== Apropos  =================================

    path('apropos/', AproposListView.as_view()),             
    path('apropos/create/', AproposCreateView.as_view()),    
    path('apropos/<int:id>/update/', AproposUpdateView.as_view()),  
    path('apropos/<int:id>/delete/', AproposDeleteView.as_view()),



    # ======================== Objectif  =================================

    path('objectif/', ObjectifListView.as_view()),             
    path('objectif/create/', ObjectifCreateView.as_view()),    
    path('objectif/<int:id>/update/', ObjectifUpdateView.as_view()),  
    path('objectif/<int:id>/delete/', ObjectifDeleteView.as_view()),


    # ======================== Projet  =================================

    path('projet/', ProjetListView.as_view()),             
    path('projet/create/', ProjetCreateView.as_view()),    
    path('projet/<int:id>/update/', ProjetUpdateView.as_view()),  
    path('projet/<int:id>/delete/', ProjetDeleteView.as_view()),


    # ======================== Commentaire  =================================

    path('commentaire/<int:activite_id>/', CommentaireListView_id.as_view())  ,          
    path('commentaire/create/', CommentaireCreateView.as_view()),    
    path('commentaire/<int:id>/update/', CommentaireUpdateView.as_view()),  
    path('commentaire/<int:id>/delete/', CommentaireDeleteView.as_view()),

    # ======================== Rapport  =================================

    path('rapport/', RapportListView.as_view()),             
    path('rapport/create/', RapportCreateView.as_view()),    
    path('rapport/<int:id>/update/', RapportUpdateView.as_view()),  
    path('rapport/<int:id>/delete/', RapportDeleteView.as_view()),

]
