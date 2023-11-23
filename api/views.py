from django.shortcuts import render
from api.models import company
from api.serializers import companyserializer
from rest_framework import viewsets

# Create your views here.
class companyviewset(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companyserializer
