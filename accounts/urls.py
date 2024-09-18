# from django.urls import path

# from .views import sign_up

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import SignUpView
from . import views

# from . import views

urlpatterns = [
    # path('signup/', views.sign_up, name="signup"),
    path('users/', views.users, name='users'),
    path('users/<int:id>/edit', views.users, name='user-edit'),
    path("signup/", SignUpView.as_view(), name="signup"),
    # path('signup/', views.sign_up, name="signup"), #get ris of this?
    # path("signup/", sign_up.as_view(), name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)