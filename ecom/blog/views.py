from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    all_articles = Blogpost.objects.all().order_by('publish_date')
    print(all_articles)
    return render (request,'blog/index.html',{'articles':all_articles})


def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render (request,'blog/blogpost.html',{'post':post})