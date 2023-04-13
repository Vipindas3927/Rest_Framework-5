from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
###################################################


from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
####################################################

from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# code-1
def hello(request):
    return JsonResponse("Hello all...", safe=False)

def dictvalue(request):
    d = {'name': 'abc', 'age': 20}
    return JsonResponse(d)

# code-2
def getdata(request):
    if request.method == "GET":
        demo = sample.objects.all()
        serializer = normalserializer(demo, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("GET method error...", safe=False)

# code-3
@csrf_exempt
def getpostdata(request):
    if request.method == "GET":
        demo = sample.objects.all()
        serializer = modelserializer(demo, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = modelserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

# code-3

@csrf_exempt
def display(request, pk):
    try:
        demo = sample.objects.get(pk=pk)
    except sample.DoesNotExist:
        return HttpResponse("Invalid")
    if request.method == 'GET':
        serializer = modelserializer(demo)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = modelserializer(demo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        demo.delete()
        return HttpResponse("Deleted Successfully")

# code-4
@api_view(['GET', 'POST'])
def get_post_api(request):
    if request.method == 'GET':
        demo = sample.objects.all()
        serializer = modelserializer(demo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = modelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_delete_api(request, pk):
    try:
        demo = sample.objects.get(pk=pk)
    except sample.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = modelserializer(demo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = modelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        demo.delete()
        return Response(status=status.HTTP_410_GONE)

# code 5

class get_post_apiview(APIView):
    def get(self, request):
        demo = sample.objects.all()
        serializer = modelserializer(demo, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = modelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_put_delete_apiview(APIView):
    def get_object(self, id):
        try:
            return sample.objects.get(id=id)
        except sample.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        demo = self.get_object(id)
        serializer = modelserializer(demo)
        return Response(serializer.data)
    def put(self, request, id):
        demo = self.get_object(id)
        serializer = modelserializer(demo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        demo = self.get_object(id)
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# code-6

# generic & mixins
class get_post_genericapiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = modelserializer
    queryset = sample.objects.all()
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class get_put_delete_genericapiView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    serializer_class = modelserializer
    queryset = sample.objects.all()
    lookup_field = 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)

class AuthView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        d = {
            'user': str(request.user)
        }
        return Response(d)