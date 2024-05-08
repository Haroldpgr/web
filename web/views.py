from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

class WebListView(View):
    def get(seft, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'web_list.html', context)

class WebCreateView(View):
    def get(self, request, *args,  **kwargs):
        context={
            
        }
        return render(request, 'web_create.html', context)
    def post(self, request, *args,  **kwargs):
        context={
            
        }
        return render(request, 'web_create.html', context)
        