from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from taggit.models import Tag
from .models import *
import json

# Create your views here.

# this is the view for login
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, "horta/llogin.html", {
                "message": "Logged in successfully",
                "msg_type": "success"
            })
        # if not authenticated
        else:
            return render(request, "horta/llogin.html", {
                "message": "Wrong Username or Password",
                "msg_type": "danger"
            })
    # if GET request
    else:
        return render(request, "horta/llogin.html")

# view for logging out
def logout_view(request):
    logout(request)
    return render(request, "horta/index.html", {
                "message": "Sessão terminada com sucesso",
                "msg_type": "danger"
            })

# view for registering
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "horta/account/register.html", {
                "message": "As palavras-passe não são iguais.",
                "msg_type": "danger"
            })
        if not username:
            return render(request, "horta/account/register.html", {
                "message": "Por favor introduza um username.",
                "msg_type": "danger"
            }) 

        if not email:
            return render(request, "horta/account/register.html", {
                "message": "Por favor introduza um email.",
                "msg_type": "danger"
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()        
            return HttpResponseRedirect(reverse("index"))

        except IntegrityError:
            return render(request, "horta/account/register.html", {
                "message": "Username ou Email já estão registados.",
                "msg_type": "danger"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    # if GET request
    else:
        return render(request, "horta/account/register.html")



def index (request):
    return render(request, 'horta/index.html')