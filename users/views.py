from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer
from django_filters import rest_framework as filters
from faker import Faker
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

fake = Faker()


# FILTER CLASS
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Users
        fields = {
        'first_name': ['icontains'],
        'last_name': ['icontains'],
        }

# API
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, edited and deleted.
    URL: http://127.0.0.1:8000/users/
    URL: http://127.0.0.1:8000/seeddb/

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


# SEED DB
@csrf_exempt 
def seedDB(request):
    if request.method == 'GET':
        count = Users.objects.count()
        return render(request, 'seeddb.html',  {'count': count})
    elif request.method == 'POST':
        # Confirm if DB is already seeded by validating that DB records are more than 100. If so, we don't need to seed the DB again
        if Users.objects.count()>=1000000:
            return render(request, 'seeding_done.html')
        else:
            names = []
            for _ in range(10000):
                names.append((fake.first_name(), fake.last_name()))
            for firstname, lastname in names:
                # Create user database objects in one query
                Users.objects.bulk_create([
                        Users(first_name=firstname, last_name=lastname),
                            ], batch_size=100)
                count = Users.objects.count()
            return render(request, 'seeding_done.html', {'count': count})