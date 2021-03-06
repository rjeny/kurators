"""kurators URL Configuration

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
from kurator_base import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.MainPage.as_view(), name='index'),
    url(r'^my/', views.MyPage.as_view(), name='mypage'),
    url(r'^kch/$', views.CursList.as_view(), name='curs'),
    url(r'^kch/done/(?P<curs>.*)$', views.CursResult.as_view(), name='curs.done'),
    url(r'^group/$', views.GroupList.as_view(), name='group'),
    url(r'^group/add/$', views.GroupAdd.as_view(), name='group.add'),
    url(r'^groups/$', views.GroupsList.as_view(), name='groups'),
    url(r'^groups/add/$', views.GroupsAdd.as_view(), name='groups.add'),
    url(r'^curators/$', views.CuratorList.as_view(), name='curators'),
    url(r'^curators/add/$', views.CuratorAdd.as_view(), name='curators.add'),
    url(r'^rating/', views.get_rating, name='rating'),
    url(r'^api/cur/get/$', views.get_curs_manual),
    url(r'^api/group/add/$', views.save_students, name='api.students.add'),
    url(r'^api/group/list/$', views.list_students, name='api.students.list')
]
