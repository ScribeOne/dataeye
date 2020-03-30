from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'hutrecord', views.HutRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('huteye/postrecording', views.HutRecordViewSet)
]
