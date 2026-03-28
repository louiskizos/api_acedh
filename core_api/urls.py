from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # ============ LogIn et Register ============================
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

]
