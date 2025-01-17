from django.shortcuts import render, redirect
from django.db import connection
from .models import Blog

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Vulnerable raw SQL query using plain-text password check (vulnerable to SQL injection)
        # Make sure the passwords in the database are stored in plain text for this to work
        query = f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'"
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchone()

        if user:
            return redirect('blog_list')  # Redirect to blog list if valid
        else:
            error = "Invalid credentials!"  # Invalid credentials message

    return render(request, 'app1/login.html', {'error': error})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'app1/blog_list.html', {'blogs': blogs})

# Homepage view
def homepage(request):
    return render(request, 'app1/homepage.html')
