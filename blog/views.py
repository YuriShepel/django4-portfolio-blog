from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


class AllPosts(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/all_blogs.html', {'posts': posts})


class Detail(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/detail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/blog/{pk}')
