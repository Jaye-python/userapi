from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = Users
        fields = ['id', 'created', 'modified', 'first_name', 'last_name',]