from django.urls import path

from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # nosotros
    path('nosotros', views.nosotros, name='nosotros'),
    # contactos
    path('contactos', views.contactos, name='contactos'),
    # inicio
    path('index', views.index, name='index'),
    # path tecnologia
    path('tecnologias', views.tecnologia, name='tecnologia'),
    # path crear
    path('tecnologias/crear', views.crear, name='crear'),
    # eliminar
    path('eliminar/<int:id_producto>', views.eliminar, name='eliminar'),
    # Editar
    path('tecnologias/editar/<int:id_producto>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
