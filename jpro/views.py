import requests
from django.http import HttpResponse
from django.utils import timezone

# from jpro.mscript.dispetch_controller import GetTournamentsJlist
import jpro.mscript.dispetch_controller as dc
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
'''
def post_list(request):
    return render(request, 'jpro/post_list.html', {})
'''


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'jpro/post_list.html', {'posts': posts})


def post_detail(request, pk):
    print('pk: ', pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'jpro/post_detail.html', {'post': post})


def jonny(request):
    return render(request, 'jpro/janix.html', {})


def controller(request):
    print('------------------------get_scipt: ')
    if request.method == "GET":
        #        client = requests.session()

        if request.GET.get('par1'):
            tournamentsJlist = dc.GetTournamentsJlist()
            return HttpResponse(tournamentsJlist, content_type='text/html')

        reqGet = request.GET.get('tid')
        if request.GET.get('tid'):
            if reqGet != '':
                MatchDetailsJList = dc.GetMatchesJlist(reqGet)
                return HttpResponse(MatchDetailsJList, content_type='text/html')

        reqGet = request.GET.get('mid')
        if reqGet:
            if reqGet != '':
                MatchDetailsJList = dc.GetMatchDetails(reqGet)
                return HttpResponse(MatchDetailsJList, content_type='text/html')
    else:
        return HttpResponse('None', content_type='text/html')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'jpro/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'jpro/post_edit.html', {'form': form})
