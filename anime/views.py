from django.shortcuts import render
import random
from django.conf import settings
import json
from django.http import JsonResponse
from pathlib import Path
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WatchListItem
from django.views.decorators.csrf import csrf_exempt
from .forms import EasySignupForm


ANIME_JSON_PATH = "anime_cache.json"


# Home page
def home(request):
    return render(request, "anime/home.html")


# About page
def about(request):
    return render(request, "anime/about.html")


# News Page
def news(request):
    return render(request, "anime/news.html")


def updates(request):
    return render(request, "anime/updates.html")


# random anime generator
def random_anime(request):
    try:
        with open(ANIME_JSON_PATH, "r", encoding="utf-8") as f:
            anime_list = json.load(f)
    except FileNotFoundError:
        return JsonResponse({"error": "anime list not found"}, status=500)

    if not anime_list:
        return JsonResponse({"error: anime list is empty"}, status=500)

    anime = random.choice(anime_list)
    return JsonResponse(anime)


# ----WatchLIst ----

# Add to watchlist
@login_required
def add_to_watchlist(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            if not title:
                return JsonResponse({"status": "error", "msg": "No title provided"}, status=400)

            WatchListItem.objects.get_or_create(user=request.user, title=title)
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "msg": str(e)}, status=500)
    return JsonResponse({"status": "error", "msg": "Invalid method"}, status=405)


# remove a show from user watchlist
def remove_from_watchlist(request, item_id):
    item = get_object_or_404(WatchListItem, id=item_id, user=request.user)
    item.delete()
    return redirect("profile")




# ----PROFILE ------

@login_required()
def profile(request):
    items = WatchListItem.objects.filter(user=request.user)
    return render(request, "anime/profile.html", {"items": items})


# ---- registration ----
def signup(request):
    if request.method == "POST":
        form = EasySignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})



