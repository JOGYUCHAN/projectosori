from django.shortcuts import get_object_or_404, render,redirect
from .forms import CommentForm, postform,Freepostform,FreeCommentForm
from .models import Post,FreePost

def home(request):
    posts = Post.objects.filter().order_by('-date')
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts,'freeposts':freeposts})    

def annonyboard(request):

    posts = Post.objects.filter().order_by('-date')
    return render(request,'anonyboard.html',{'posts':posts})


def fashionboard(request):  
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request,'fashionboard.html',{'freeposts':freeposts})


def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('annoyboard')
    else:
        form=postform()
    return render(request,'post_form.html',{'form':form})    

def detail(request,post_id):
    post_detail=get_object_or_404(Post,pk=post_id)
    comment_form=CommentForm() 
    return render(request,'detail.html',{'post_detail':post_detail,'comment_form':comment_form})

def new_comment(request,post_id):
    filled_form=CommentForm(request.POST)
    if filled_form.is_valid:
        finished_form=filled_form.save(commit=False)
        finished_form.post=get_object_or_404(Post,pk=post_id)
        finished_form.save()
    return redirect('detail',post_id)

def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = Freepostform(request.POST, request.FILES)
        if form.is_valid():
            unfinished=form.save(commit=False)
            unfinished.author=request.user
            unfinished.save()
            return redirect('fashionboard')
    else:
        form=Freepostform()
    return render(request,'freepost_form.html',{'form':form})    

def freedetail(request,post_id):
    post_detail=get_object_or_404(FreePost,pk=post_id)
    comment_form=FreeCommentForm() 
    return render(request,'freedetail.html',{'post_detail':post_detail,'comment_form':comment_form})

def new_freecomment(request,post_id):
    filled_form=FreeCommentForm(request.POST)
    if filled_form.is_valid:
        finished_form=filled_form.save(commit=False)
        finished_form.post=get_object_or_404(FreePost,pk=post_id)
        finished_form.save()
    return redirect('freedetail',post_id)

