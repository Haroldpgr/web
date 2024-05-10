from django.shortcuts import   get_object_or_404, render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

class WebListView(View):
    def get(seft, request, *args, **kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts
            
        }
        return render(request, 'web_list.html', context)

class WebCreateView(View):
    def get(self, request, *args,  **kwargs):
        form = PostCreateForm()
        
        context={'form': form
            
        }
        return render(request, 'web_create.html', context)
    def post(self, request, *args,  **kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                
                return redirect('web:home')
            pass
        context={
            
        }
        return render(request, 'web_create.html', context)
    
class WebDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post': post
        }
        return render(request, 'web_detail.html', context)
    