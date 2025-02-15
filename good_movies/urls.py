"""good_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from movies import views #NOWE
from django.contrib.auth.views import LoginView, LogoutView
from movies.views import ZeroConfigurationDatatableView 

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.my_profile, name='my_profile'),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('index/', views.index, name='index'), #nowe
    path('subpage/', views.subpage),
    path('filmy/', views.list_movies),
    path('', views.hello),
    path('accounts/signup/', views.user_signup, name='user_signup'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html')),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('topmovies/', ZeroConfigurationDatatableView.as_view(), name="top_movies"),
]
