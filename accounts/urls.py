from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import  views as auth_views


from . import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('', account_views.UserDetailView.as_view(), name='account_detail'),
    path('signup/', account_views.UserCreateView.as_view(), name='account_signup'),
    path('login/', account_views.UserLoginView.as_view(), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
]