from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.utils import timezone
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.models import Post,Comment
from blog_app.forms import PostForm,CommentForm

# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post_detail'


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog_app:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


##############################

def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('blog_app:post_list')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('blog_app:post_detail',pk = post.pk)
    else:
        form = CommentForm()
    return render(request,'blog_app/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approved_comment = True
    comment.save()
    return redirect('blog_app:post_detail',pk=comment.post.pk)

@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog_app:post_detail',pk = post_pk)