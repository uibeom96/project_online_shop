from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from users.models import User

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            del(form.cleaned_data["password2"])
            User.objects.create_user(**form.cleaned_data)
            return redirect("shop:products_list")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})