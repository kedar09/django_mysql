from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from user.models import User

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status

# Create your views here.


def adduser(request):
    # form = (request.POST)
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    # print(request.POST['name'])
    add_user = User.objects.create(
        name=name,
        email=email,
        contact=contact,
    )
    print(add_user)
    return HttpResponse({'message: created'}, content_type="application/json")


def showalluser(request):
    data = serializers.serialize('json', User.objects.all())
    return HttpResponse(data, content_type="application/json")
    

def updateuser(request, id):
    user_form = User.objects.get(id=id)
    user_form.name = request.POST['name']
    user_form.email = request.POST['email']
    user_form.contact = request.POST['contact']
    print(user_form)
    user_form.save()
    return HttpResponse({'message: updated'}, content_type="application/json")


def deleteuser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponse({'message: deleted'}, content_type="application/json")

# Create your views here.
