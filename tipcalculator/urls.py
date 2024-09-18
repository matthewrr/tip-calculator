from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('getdata.urls')),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("reports/", include("reports.urls")),
    
    # path('signup/', views.sign_up),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
