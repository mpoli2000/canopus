from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'stars/home.html'
    ordering = ['-post_date']

def LikeView(request, pk):
    print(request.POST)
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    print(post)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('stars:article-detail', args=[str(pk)]))

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'stars/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'stars/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'stars/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'stars/delete_post.html'
    success_url = reverse_lazy('stars:home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stars/add_comment.html'
    success_url = reverse_lazy('stars:home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
