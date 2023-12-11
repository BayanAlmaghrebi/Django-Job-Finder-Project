from rest_framework import serializers
from .models import Jobs , Company 


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'