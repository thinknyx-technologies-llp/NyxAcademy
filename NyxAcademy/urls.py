"""
URL configuration for NyxAcademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('nyx-admin/', admin.site.urls),
    path('home/', user_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('youtube/', user_views.youtube, name='youtube'),
    path('books/', user_views.books, name='books'),
    path('', user_views.login, name='login'),
    # path('register/', user_views.signup, name='signup'),
]
