from django.urls import include, re_path, path
from rest_framework import routers

from .views import ImageProcessAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('detect-objects/', ImageProcessAPIView.as_view(), name='detect-objects'),
]
