from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()