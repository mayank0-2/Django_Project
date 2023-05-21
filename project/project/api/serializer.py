from user.models import post
from django.shortcuts import render
from rest_framework.serializers import ModelSerializer



class postserializer(ModelSerializer) :

    class Meta :
        model = post
        fields = ['user_name', 'post_title', 'post_content', 'date_published', 'user_profile_link']
