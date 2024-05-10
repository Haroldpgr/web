from django.urls import path
from .views import  WebListView, WebCreateView, WebDetailView 
app_name= "web"
urlpatterns = [
    path('', WebListView.as_view(), name=('home')),
    path('create/', WebCreateView.as_view(), name='create'),
    path('<int:pk>/', WebDetailView.as_view(), name='detail')
]   
