
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")




# ///////


# class SignUpForm(UserCreationForm):
#     class Meta:
#         # model = User
#         model = CustomUser
#         # fields = ['first_name', 'last_name', 'email']
#         fields = ['email']
#         labels = {'email': 'Email'}

# class CustomUserCreationForm(UserCreationForm):
#     """Extending default user creation form"""

#     class Meta:
#         #Use our user model in creationform
#         model = CustomUser
