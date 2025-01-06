from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:20]  # Display the first 20 characters of the comment
