
# from django.contrib import admin
# from django.urls import include, path
# from django.conf import settings
# from django.conf.urls.static import static



# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('core_api.urls')),
# # ] 
# # if settings.DEBUG:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # On met l'inclusion de l'API après
# urlpatterns += [path('', include('core_api.urls'))]


# from django.contrib import admin
# from django.urls import include, path
# from django.conf import settings
# from django.conf.urls.static import static

# # 1. On définit d'abord les routes de base (admin)
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# # 2. On ajoute les médias TOUT DE SUITE après si on est en DEBUG
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # 3. On ajoute l'inclusion de ton API à la fin
# urlpatterns += [
#     path('', include('core_api.urls')),
# ]

# --- api_acedh/urls.py ---
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# FORÇAGE DES MÉDIAS (Même si DEBUG est capricieux)
media_url_patterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += media_url_patterns

# Affichage des infos dans ton terminal au lancement
print("\n" + "="*30)
print(f"VALEUR DE DEBUG : {settings.DEBUG}")
print(f"MEDIA_URL : {settings.MEDIA_URL}")
print(f"Dossier MEDIA_ROOT : {settings.MEDIA_ROOT}")
print(f"Nombre de routes MEDIA détectées : {len(media_url_patterns)}")
print("="*30 + "\n")

# Ton API à la fin
urlpatterns += [
    path('', include('core_api.urls')),
]