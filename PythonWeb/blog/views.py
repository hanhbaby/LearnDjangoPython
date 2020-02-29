from django.shortcuts import render, get_object_or_404
from  blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request, author=request.user, post=post)
        print("debugggggaaa")
        #if form.is_valid():
        print("debuggggg")
        form.save()
        return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post":post, "form":form})
