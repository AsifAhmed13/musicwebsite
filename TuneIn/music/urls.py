from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("music/login/",views.login_view,name="login"),
    path("music/signup/",views.signup_view,name="signup"),
    path("music/logout/",views.logout_view,name="logout"),
    path("add",views.add_album,name="add"),
]