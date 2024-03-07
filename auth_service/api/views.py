from rest_framework import viewsets

from api.models import Company
from api.serializers import CompanySerializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
