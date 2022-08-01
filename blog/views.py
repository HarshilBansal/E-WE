from django.shortcuts import render

from .models import Post
# Create your views here.
def home(request):
    data = Post.objects.all()
    print(data)
    return render(request,'index.html',{"posts": data})


def single(request,slug):
    data = Post.objects.get(slug=slug)
    print(data)
    return render(request,'single.html',{"post": data})
    # return render(request,'index.html',{})
