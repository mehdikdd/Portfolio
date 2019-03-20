from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
import requests

def allblogs(request):
    a=requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    blogs = Blog.objects
    z=str(a.json()['data']['amount'])
    return render(request, 'blog/allblogs.html', {'blogs': blogs, 'z' : z } )

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})