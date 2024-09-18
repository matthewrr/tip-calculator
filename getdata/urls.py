from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.find_item, name='home'),
    path('validate/', views.validate_data, name='validate_data'),
    path('support/', views.support, name='support'),
    # path('reports/', views.reports, name='reports'), #move to reports app
    # path('ajax/get_data/', views.get_data, name='get_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)