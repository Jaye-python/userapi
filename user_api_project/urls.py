from posixpath import basename
from django.urls import include, path
from rest_framework import routers
from users import views
from django.contrib import admin
from django.urls import path


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
