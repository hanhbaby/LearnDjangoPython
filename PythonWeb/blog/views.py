from django.shortcuts import render, get_object_or_404
from  blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from pprint import pprint

# Create your views here.
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post":post, "form":form})


def update_comment(request):
  print(request.POST)
  #1)Dữ liệu
  #1.1)Request
  param_comment = request.POST["comment"]
  
  #1.2)DB

  #2)Xử lý
  #2.1)Lấy list comment
  list_comment = param_comment.split(' ')

  #3)Trả về
  data = {
    'list_comment' : list_comment
  }
  return render(request,'blog/table.html',data)