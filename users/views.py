from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer
from django_filters import rest_framework as filters


# FILTER CLASS
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Users

        fields = {
        'first_name': ['icontains'],
        'last_name': ['icontains'],
        }

# MODEL
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, edited and deleted.
    URL: http://127.0.0.1:8000/users/

    You may filter using case INsenSITIve names:
    Filter URL: http://127.0.0.1:8000/users/?first_name=jo
    Filter URL: http://127.0.0.1:8000/users/?first_name=jo&last_name=pa
    Docs URL: http://127.0.0.1:8000/api/schema/swagger-ui/
    2nd Docs URL: http://127.0.0.1:8000/api/schema/redoc
    YAML Docs URL: http://127.0.0.1:8000/api/schema/

    """
    queryset = Users.objects.all().order_by('-created')
    serializer_class = UserSerializer
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'id', 'created']
    filterset_class = ProductFilter
