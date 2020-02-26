from django.shortcuts import render
from  .models import Post
# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by("_date")}
    return render(request, 'blog/blog.html', Data)