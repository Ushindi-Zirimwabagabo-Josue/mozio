from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon, Point
from .serializers import ProviderModelSerializer, ServiceAreaModelSerializer, QuerySerializer
from .models import Provider, ServiceArea

# Create your views here.

@api_view(['GET'])
def documentation(request):
    api_documentation = [
        {
            'Endpoint' : '/api/v1/providers',
            'method' : 'GET',
            'body' : None ,
            'description' : 'Returns all Providers'
        },
        {
            'Endpoint' : '/api/v1/providers/id',
            'method' : 'GET',
            'body' : None ,
            'description' : 'Returns a single Provider by id'
        },
        {
            'Endpoint' : '/api/v1/providers/add',
            'method' : 'POST',
            'body' : {
                "name": "name",
                "email": "jo@gmail.com",
                "phone_number": "+250789816999",
                "language": "language",
                "currency": "USD"
                } ,
            'description' : 'Create Provider'
        },
        {
            'Endpoint' : '/api/v1/providers/1',
            'method' : 'PUT',
            'body' : {
                "name": "jose",
                "email": "jose@gmail.com",
                "phone_number": "+250789811119",
                "language": "language",
                "currency": "USD"
                } ,
            'description' : 'Update Provider information'
        },
        {
            'Endpoint' : '/api/v1/providers/1',
            'method' : 'PATCH',
            'body' : {
                "email": "josemary@gmail.com"
                } ,
            'description' : 'Update a specific Provider information'
        },
        {
            'Endpoint' : '/api/v1/providers/1',
            'method' : 'DELETE',
            'body' : None ,
            'description' : 'Deletes a Provider from the Database'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas',
            'method' : 'GET',
            'body' : None ,
            'description' : 'Returns all Service Areas'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas/3',
            'method' : 'GET',
            'body' : None ,
            'description' : 'Returns service area by id'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas/add',
            'method' : 'POST',
            'body' : {
                "name" : "name of the Service Area",
                "price" : "200",
                "geojson" :  "To be obtain at geojson.io",
                "provider" :  "Al"
            },
            'description' : 'Creates a Service Area'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas/3',
            'method' : 'PUT',
            'body' : {
                "name" : "Somewhere",
                "price" : "1200",
                "area" :  "To be obtain at geojson.io",
                "provider" :  "Omar"
            },
            'description' : 'Updates a Service Area already on the Database'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas/3',
            'method' : 'PATCH',
            'body' : {
                "name" : "Somewhere"            
                } ,
            'description' : 'Updates a Service Area Detail'
        },
        {
            'Endpoint' : '/api/v1/serviceAreas/3',
            'method' : 'DELETE',
            'body' : None ,
            'description' : 'Deteles a Service Area'
        },
        {
            'Endpoint' : '/api/query?lat=12&lng=-12',
            'method' : 'GET',
            'body' : None ,
            'description' : 'Returns a list of all polygons that include the given lat/lng'
        }
    ]
    return Response(api_documentation)

class ProviderAll(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderModelSerializer

class ServiceAreaAll(generics.ListAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

class ServiceAreaList(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaModelSerializer

@api_view(['GET'])
def query(request):

    '''Retrieve all polygons that contain the point of latitude and longitud specified'''

    lat = float(request.GET.get('lat', None))
    lng = float(request.GET.get('lng', None))

    if lat is None or lng is None:
        return Response('Data is incomplete, please add lat and lng. ')

    # print(type(lat))
    point = Point(lat,lng)
    # print(point)

    matchPolygons = ServiceArea.objects.filter(geojson__contains=point)

    if len(matchPolygons) == 0:
        return Response("No service provider registered in the polygon area.")


    serializer = QuerySerializer(matchPolygons, many=True)
    return Response(serializer.data)