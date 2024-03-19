from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("login", views.loginpage, name="login"),
    path("signup", views.signuppage, name="signup"),
    path("logout/", views.logoutpage, name="logout"),
    path("about", views.about, name="about"),
    path("joinus", views.joinus, name="joinus"),
    path("community", views.community, name="community"),
    path("performance", views.performance, name="performance"),
    path("rankboard", views.rankboard, name="rankboard"),
    path("viewtests", views.viewtests, name="viewtests"),
    path('taketest', views.taketest, name='taketest'),
    path('testanalysis', views.testanalysis, name='testanalysis'),
]
