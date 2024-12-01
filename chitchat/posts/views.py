from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associate the post with the logged-in user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Update an existing post
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:  # Check if the logged-in user is the owner of the post
        return redirect('post_detail', post_id=post.id)  # Redirect if user is not the owner
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form, 'post': post})

# Delete a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:  # Only the owner can delete the post
        post.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return redirect('post_detail', post_id=post.id)  # Redirect if user is not the owner


# Like a post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({"liked": liked, "total_likes": post.total_likes()})

# Save a post
@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.saves.filter(id=request.user.id).exists():
        post.saves.remove(request.user)
        saved = False
    else:
        post.saves.add(request.user)
        saved = True
    return JsonResponse({"saved": saved, "total_saves": post.total_saves()})

# Like a comment
@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        liked = False
    else:
        comment.likes.add(request.user)
        liked = True
    return JsonResponse({"liked": liked, "total_likes": comment.total_likes()})

# Add a comment to a post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get('content')
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        return redirect('post_detail', post_id=post.id)  # Redirect to post detail page (you can create a post detail view for this)
    return render(request, 'comment_form.html', {'post': post})