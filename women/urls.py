from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('',index, name = 'home'),
    path('about/', about, name = 'about'),
    path('addpage/', addpage, name = 'add_page'),
    path('contact/', about, name = 'contact'),
    path('login/', about, name = 'login'),
    path('post/<int:post_id>/',show_post,name = 'post')
]