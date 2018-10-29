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
from django.conf.urls import url
from django.contrib import admin
from movies.views import MovieAdd,MovieListView,MovieDetail,UpdateMovie,MovieListHome,ShowAdd,ShowListView,UpdateShow,ScreenAdd,ScreenListView,UpdateScreen,DeleteMovie,DeleteShow,DeleteScreen
from movies.views import CarousalAdd,CarousalListView,UpdateCarousal


urlpatterns = [

url(r'^home/',MovieListHome.as_view(),name='m_lst_hme'),

url(r'^m_add/',MovieAdd.as_view(), name='movies_add'),
url(r'^mlstview/',MovieListView.as_view(),name='m_lstview'),
url(r'^mdetail/(?P<pk>[0-9]+)/$',MovieDetail.as_view(),name='m_d_view'),
url(r'^mupdate/(?P<pk>[0-9]+)/$',UpdateMovie.as_view(),name='m_up_view'),
url(r'^mdelete/(?P<pk>[0-9]+)/$',DeleteMovie.as_view(),name='m_del_view'),

# url(r'^bview/',BaseView.as_view(),name='b_view'),

url(r'^s_add/',ShowAdd.as_view(), name='s_add'),
url(r'^slview/',ShowListView.as_view(),name='s_lstview'),
url(r'^supdate/(?P<pk>[0-9]+)/$',UpdateShow.as_view(),name='s_up_view'),
url(r'^sdelete/(?P<pk>[0-9]+)/$',DeleteShow.as_view(),name='s_del_view'),

url(r'^sc_add/',ScreenAdd.as_view(), name='sc_add'),
url(r'^sclview/',ScreenListView.as_view(),name='sc_lstview'),
url(r'^scupdate/(?P<pk>[0-9]+)/$',UpdateScreen.as_view(),name='sc_up_view'),
url(r'^scdelete/(?P<pk>[0-9]+)/$',DeleteScreen.as_view(),name='sc_del_view'),

url(r'^c_add/',CarousalAdd.as_view(), name='carousal_add'),
url(r'^clstview/',CarousalListView.as_view(),name='c_lstview'),
url(r'^cupdate/(?P<pk>[0-9]+)/$',UpdateCarousal.as_view(),name='c_up_view'),


]