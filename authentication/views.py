from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account Created successfully. You can login now!"
            )
            return redirect("login")
    else:
        form = forms.UserRegisterForm()
    return render(request, "auth.html", {"form": form, "type": "Register"})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                print("YES")
                login(request, user)
                messages.success(request, "Logged In Successfully!")
                return redirect("profile")
            else:
                messages.warning(request, "Invalid Username or password!")
                return redirect("login")
    else:
        form = AuthenticationForm()
    return render(request, "auth.html", {"form": form, "type": "Login"})


@login_required()
def user_profile(request):
    if request.method == "POST":
        form = forms.UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
    else:
        form = forms.UserUpdateForm(instance=request.user)
    return render(request, "profile.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully!")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(
        request, "change_password.html", {"form": form, "type": "Change Password"}
    )


@login_required
def change_password2(request):
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully!")
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(
        request, "change_password.html", {"form": form, "type": "Change Password"}
    )


@login_required()
def user_logout(request):
    logout(request)
    messages.warning(request, "Logged Out Successfully!")
    return redirect("home")
