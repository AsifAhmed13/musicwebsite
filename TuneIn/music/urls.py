from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("music/login/",views.login_view,name="login"),
    path("music/signup/",views.signup_view,name="signup"),
    path("music/logout/",views.logout_view,name="logout"),
    path("add/",views.add_album,name="add"),
    path("music/songs/",views.mysongs,name="mysongs"),
    path("music/songs/<str:album_title>/<str:song_name>/",views.playsongs,name="playsongs"),
    path("<str:album_title>/",views.details,name="details"),
    path("<str:album_title>/delete/",views.deletealbum,name="delete"),
    path("<str:album_title>/<str:song_name>/play/",views.playsong,name="playsong"),
    path("<str:album_title>/<str:song_name>/deletesong/",views.deletesong,name="deletesong"),
    path("<str:album_title>/addsong/",views.addsong,name="addsong"),
]