from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Blog
from django.views.decorators.csrf import csrf_exempt

# Vulnerable login view (for demonstration purposes)
@csrf_exempt
def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Use Django's authenticate method, which handles hashed passwords
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in and redirect to the blog list page
            login(request, user)
            return redirect('blog_list')
        else:
            error = "Invalid credentials!"
    
    return render(request, 'app1/login.html', {'error': error})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'app1/blog_list.html', {'blogs': blogs})


# Homepage view
def homepage(request):
    return render(request, 'app1/homepage.html')  # Render homepage template


