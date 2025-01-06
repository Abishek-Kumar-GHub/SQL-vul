from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),  # Add this
    path('login/', views.vulnerable_login, name='login'),
    path('detail/<int:pk>/', views.blog_detail, name='blog_detail'),
]
