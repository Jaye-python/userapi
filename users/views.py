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
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-created')
    serializer_class = UserSerializer
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'id', 'created']
    filterset_class = ProductFilter
