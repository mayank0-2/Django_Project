from django.shortcuts import render
from user.models import post
from . serializer import postserializer
from rest_framework.viewsets import ModelViewSet



# Create your views here.


class PostViewSet(ModelViewSet) :
    queryset = post.objects.all().order_by('id')[:10]
    serializer_class = postserializer
