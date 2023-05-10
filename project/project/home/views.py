from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from user.models import post

# Create your views here.

def home (request) :
    context1  = {'post' : post.objects.all()}
    return render (request, 'home_page.html', context1)


class PostListView (ListView) :

    model = post
    template_name = 'home_page.html'
    context_object_name = 'post'
    ordering = ['date_published']
