from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article


def frontpage(request):
    posts = Article.objects.all()

    return render(request, 'frontpage.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def post_detail(request, slug):
    post = Article.objects.get(slug=slug)

    return render(request, 'post_detail.html', {'post': post})
