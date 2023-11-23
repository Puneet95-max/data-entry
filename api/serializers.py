from rest_framework import serializers
from api.models import company

class companyserializer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField()
    class Meta:
        model=company
        fields="__all__"
