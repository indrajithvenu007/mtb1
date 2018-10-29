"""mtb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts.views import UserAdd,UserListView
from accounts import views


urlpatterns = [

url(r'^u_add/',UserAdd.as_view(), name='user_add'),
url(r'^ulview/',UserListView.as_view(),name='u_lstview'),
url(r'^login/$',views.login, name='login'),
url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
url(r'^oauth/', include('social_django.urls', namespace='social')),



]