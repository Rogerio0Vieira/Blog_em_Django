from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'post': posts})


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})
