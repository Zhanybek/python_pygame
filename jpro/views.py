from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from jpro.mscript.script01 import scriptJ
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
    print('pk: ',pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'jpro/post_detail.html', {'post': post})

def jonny(request):
#    jsondataL = scriptJ()
    print('------------------------taki jonny ')
    return render(request, 'jpro/janix.html', {})

'''
def get_scipt(request):
    print('------------------------get_scipt: ')
    jsondataL = scriptJ()
    return render(request, 'jpro/janix.html', {'reft': jsondataL})
'''

def get_scipt(request):
    print('------------------------get_scipt: ')
    if request.method == "GET":
        print('------------------------GET: ', request.GET.get('par1'))
        jsondataL = scriptJ()
#        request.session['view'] = request.GET['view']
        return HttpResponse(jsondataL, content_type='text/html')
    else:
        print('------------------------else: ')
        return HttpResponse('no', content_type='text/html')


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
