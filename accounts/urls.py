from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_Views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',auth_Views.LoginView.as_view(template_name = 'account/login.html'),name = 'login'),
    path('logout/',auth_Views.LogoutView.as_view(),name = 'logout'),
    path('SignUp',views.SignUp.as_view(),name = 'signup'),
]
