from django.shortcuts import render, get_object_or_404
from .models import News

def home_page(request):
    posts = News.objects.all().order_by('-date')[:4]
    context = {'posts': posts}
    return render(request, './index.html', context)

def news_page(request):
    posts = News.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, './news-list.html', context)

def details_page(request, pk):
    post = get_object_or_404(News, pk=pk)
    context = {'post': post}
    return render(request, './news-detail.html', context)

