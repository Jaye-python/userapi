from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='users-detail', read_only=True)
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = Users
        fields = ['id', 'url', 'created', 'modified', 'first_name', 'last_name',]