from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from reports import myplot

urlpatterns = [
    # path('reports/', views.reports, name='reports'),
    # path('', include('getdata.urls')),
    # path("reports/", include("reports.urls"), name="reports"),
    path('', views.reports, name='reports'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    path("signup/", SignUpView.as_view(), name="signup"),

    # path('admin/', admin.site.urls),
    # path('', include('getdata.urls')),
    # path("accounts/", include("accounts.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),