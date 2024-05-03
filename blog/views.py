from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.views import generic

from .forms import PostForm
from .models import Post


# *** functional view post list view ***
# def post_list_view(request):
#     # posts = Post.objects.all()
#     posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts})

# *** class base view for post list view ***
class PostListView(generic.ListView):
    # model = Post *** for all objects without method or filter
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'
#     for set custom query and no model data
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

# *** functional view post list view ***

# def post_detail_view(request, pk):
#    test
#     # print('ID IN URL: ', pk)
#     # return HttpResponse(f'ID: {pk}')
#     # try:
#     #     detail = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     detail = None
#     #     print('No such post')
#     detail = get_object_or_404(Post,pk=pk)
#     return render(request, 'blog/post_detail.html', context={'post_detail': detail})

# *** class base view for post detail view ***
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'

# *** functional view for post_create_view ***
# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#
#     else:
#         form = PostForm()
#     return  render(request, 'blog/post_create.html' , context={'form': form})

# *** class base view for post create view ***
class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     author = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=author, status='pub')
    # else:
    #     print('GET req')

    # return render(request , 'blog/post_create.html')
# *** functional view for post_update_view ***

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None ,instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_create.html', context={'form': form})

    # *** class base view for post list view ***
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'

# *** functional view for post_delete_view ***

# def post_delete_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})

# *** class base view for post delete view ***

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')
