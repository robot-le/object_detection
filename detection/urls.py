from django.urls import include, re_path, path
from rest_framework import routers

from .views import ImageProcessAPIView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('detect-objects/', ImageProcessAPIView.as_view(), name='detect-objects'),
]
