""" URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
#router.register(r'hutrecord', views.HutRecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('records/', views.HutRecordView.as_view()),
    path('report/', views.report),
    path('dev/', views.Dev.as_view()),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('user/', views.user),
    path('userdevice/', views.userdevice),
    url(r'^devicerecord/(?P<id>[0-9]+)/$', views.devicerecord),
]
