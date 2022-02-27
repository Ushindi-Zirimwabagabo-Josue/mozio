from rest_framework import serializers
from .models import ServiceArea, Provider

class ProviderModelSerializer(serializers.ModelSerializer):

    '''Serializer for Provider model'''

    class Meta:
        model = Provider
        fields = '__all__'

class ServiceAreaModelSerializer(serializers.ModelSerializer):

    '''Serializer for ServiceArea model'''

    class Meta:
        model = ServiceArea
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):

    '''Serializer for Query model'''

    class Meta:
        model = ServiceArea
        fields = ['provider','name', 'price']