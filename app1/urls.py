from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),  # Add this
    path('login/', views.login_view, name='login'),
]
