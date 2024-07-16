from django.shortcuts import render
from django.views import View
from .models import Post
# Create your views here.

class Home(View):
    def get(self,request):
        context={
            'posts':Post.objects.all()
        }
        return render(request,'blog/home.html',context)

class About(View):
    def get(self,request):
        return render(request,'blog/about.html',{'title':'About'})
     