from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IgViewSet
router = DefaultRouter()
router.register(r'messages', IgViewSet, basename='message')
urlpatterns = [
    path('', include(router.urls))
]
