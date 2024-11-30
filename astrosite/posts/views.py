import os

from django.conf import settings

from astrosite.posts.forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


def posts_list_view(request):

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts_list.html', {'posts': posts})

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_detail_view(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():

                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, "Your comment was added successfully.")
                return redirect('post_detail', pk=post.pk)
        else:
            messages.warning(request, "You need to log in to add a comment.")
            return redirect('login')
    else:
        form = CommentForm()


    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comment_form': form
    })


@login_required
def post_edit_view(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.warning(request, "You are not authorized to edit this post.")
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})



@login_required
def post_delete_view(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.warning(request, "You are not authorized to delete this post.")
        return redirect('post_detail', pk=post.pk)
    if post.image:

            image_path = os.path.join(settings.MEDIA_ROOT, post.image.name)


            if os.path.isfile(image_path):
                os.remove(image_path)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')

    return render(request, 'posts/post_delete.html', {'post': post})
