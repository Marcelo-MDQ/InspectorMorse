from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('capitulos', views.capitulos, name='capitulos'),
    path('resenia/<int:id>/',views.reseniaCapitulo, name = 'resenia_Capitulo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
