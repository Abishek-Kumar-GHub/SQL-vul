from django.shortcuts import render, redirect
from django.db import connection
from .models import Blog, Comment

# Vulnerable login view (for demonstration purposes)
def vulnerable_login(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        query = f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchone()
        if user:
            return redirect('blog_list')  # Assuming 'blog_list' exists, but we will add this later
        else:
            error = "Invalid credentials!"

    return render(request, 'app1/login.html', {'error': error})

# Blog detail view (with vulnerability to XSS)
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        comment_content = request.POST['comment']     #If the comment_content is displayed on the page without sanitization, attackers can inject malicious JavaScript.
        Comment.objects.create(blog=blog, content=comment_content)
    comments = blog.comments.all()
    return render(request, 'app1/detail.html', {'blog': blog, 'comments': comments})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'app1/blog_list.html', {'blogs': blogs})


# Homepage view
def homepage(request):
    return render(request, 'app1/homepage.html')  # Render homepage template
