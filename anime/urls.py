from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("news/", views.news, name="news"),
    path("updates/", views.updates, name="updates"),

    path("api/random/", views.random_anime, name="random_anime"),
    path("watchlist/add/", views.add_to_watchlist, name="add_to_watchlist"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("remove/<int:item_id>/", views.remove_from_watchlist, name="remove_from_watchlist"),

]


