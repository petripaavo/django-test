import random
import string
from django.db import models

def generate_anon_name():
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    return f'anon_writer{suffix}'

class Post(models.Model):
    author = models.CharField(max_length=50, blank=True, default=generate_anon_name)
    text = models.TextField()
    media = models.FileField(upload_to='media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Post {self.id} by {self.author}"
