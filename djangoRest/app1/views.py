from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

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



