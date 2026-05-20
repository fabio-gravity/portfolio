from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registo/', views.registo_view, name="registo"),
    path('magic-link/', views.magic_link_request_view, name="magic_link"),
    path('magic-login/<str:token>/', views.magic_link_login_view, name="magic_login"),
]
