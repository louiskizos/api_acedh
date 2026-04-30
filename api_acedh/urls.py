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