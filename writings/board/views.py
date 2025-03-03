from django.shortcuts import render, redirect
from .models import Post

def board_view(request):
    posts = Post.objects.filter(parent__isnull=True).order_by('-created_at')
    return render(request, 'board/board.html', {'posts': posts})

def post_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.POST.get('author', '').strip()
        parent_id = request.POST.get('parent_id', None)
        media = request.FILES.get('media')

        if not author:
            author = Post().author  # Generate random anonymous name

        parent = Post.objects.get(id=parent_id) if parent_id else None
        Post.objects.create(text=text, author=author, media=media, parent=parent)
        return redirect('board')

    return redirect('board')
