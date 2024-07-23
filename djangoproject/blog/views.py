from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
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
     
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'

    ordering=['-date_posted']
    paginate_by=5


class PostDetailView(DetailView):
    model=Post



class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

     
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/"


    def test_func(self) -> bool | None:
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self) -> QuerySet[Any]:
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')