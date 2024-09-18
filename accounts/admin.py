from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # fields = ["default_role"]
    # list_display = ["email", "username", "default_role"]


    list_display = ("__str__", "email", "phone_number", "is_staff", "is_active", "default_role")
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "default_role", "email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    # add_fieldsets = (
    #     (None, {
    #         "classes": ("wide",),
    #         "fields": (
    #             "email", "password1", "password2", "is_staff",
    #             "is_active", "groups", "user_permissions"
    #         )}
    #     ),
    # )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

# class PersonAdmin(admin.ModelAdmin):
#    fields = (
#        'active',
#        'first_name',
#        'last_name',
#        'preferred_name',
#        'default_role',
#        'email_address',
#        'phone_number',
#        'created_date',
#    )
#    list_display = (
#        'active',
#        'first_name',
#        'last_name',
#        'preferred_name',
#        'default_role',
#        'email_address',
#        'phone_number',
#        'created_date',
#       )

# admin.site.register(Person, PersonAdmin)