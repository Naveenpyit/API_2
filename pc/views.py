from django.shortcuts import render
from .models import product
from .serializer import prodserializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import authentication_classes
from .authentication import apikeycheck 


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([apikeycheck ])
def main_view(request,id=0):
    print("API key passed Sucessfully")
    if request.method=='GET':
        return get_view(request)
    elif request.method=='POST':
        return post_view(request)
    elif request.method=='PUT':
        return put_view(request,id)
    elif request.method=='DELETE':
        return delete_view(request,id)
    

def get_view(request):
    prod_id=request.GET.get('id',None)
    if prod_id:
        try:
            prod=product.objects.get(product_id=prod_id)
            prod_serial=prodserializer(prod)
            return JsonResponse(prod_serial.data,safe=False)
        except product.DoesNotExist:
            return JsonResponse({"message":"Product doesn't exists"},status=404) 
    else:
        prod=product.objects.all()
        prod_serial=prodserializer(prod,many=True)
        return JsonResponse(prod_serial.data,safe=False)
               
def post_view(request):
    prod=JSONParser().parse(request)
    prod_serial=prodserializer(data=prod)
    if prod_serial.is_valid():
        prod_serial.save()
        return JsonResponse({"message":"Created Succesfully","data":prod_serial.data},status=201) 
    return JsonResponse({"message":"Failed to create","data":prod_serial.errors},status=404)

def put_view(request,id):
    prod=JSONParser().parse(request)
    try:
        prods=product.objects.get(product_id=id)
        prod_serial=prodserializer(prods,data=prod)
        if prod_serial.is_valid():
            prod_serial.save()
            return JsonResponse({"message":"Updated Successfully","data":prod_serial.data},status=201)
    except product.DoesNotExist:
        return JsonResponse({"message":"Product doesn't exists","data":prod_serial.errors},status=404)

def delete_view(request,id):
   try:
        prods=product.objects.get(product_id=id)
        prods.delete()
        return JsonResponse({"message":"Deleted Successfully"},status=201)
   except product.DoesNotExist:
       return JsonResponse({"message":"Product doesn't exists"},status=404)

