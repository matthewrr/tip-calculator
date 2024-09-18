from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserChangeForm


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def users(request):
    employees = CustomUser.objects.order_by('first_name')
    context = {"title": "Users", "employees": employees}
    return render(request, 'accounts/users.html', context)

# listings/views.py

# def user_update(request, id):
#     band = CustomUser.objects.get(id=id)
#     form = BandForm(instance=band)  # prepopulate the form with an existing band
#     return render(request, 'accounts/users_edit.html', {'form': form})

def user_update(request, id):
    print(id)
    print("Printed ID")
    user = CustomUser.objects.get(pk=id)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return #redirect('band-detail', band.id))
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'accounts/users_edit.html', {'form': form})