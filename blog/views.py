from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.


def blogList(request):

    posts = BlogPost.objects.all().order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog_list.html', context)


def blogDetail(request, slug):

    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog_detail.html', context)