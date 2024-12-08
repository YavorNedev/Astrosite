from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Thread, Comments
from .forms import ThreadForm, CommentForm



def category_list_view(request):
    categories = Category.objects.all()  # Corrected query
    return render(request, 'forum/category_list.html', {'categories': categories})

def thread_list_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Corrected model reference
    threads = Thread.objects.filter(category=category)

    context = {
        'category': category,
        'threads': threads,
    }
    return render(request, 'forum/thread_list.html', context)

@login_required
def create_thread_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Corrected model reference
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.category = category
            thread.save()
            return redirect('thread_list', category_id=category.id)
    else:
        form = ThreadForm()
    return render(request, 'forum/thread_form.html', {'form': form, 'category': category})

def thread_detail_view(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    comments = thread.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.thread = thread
            comment.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = CommentForm()
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'comments': comments, 'form': form})

