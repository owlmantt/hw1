from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from django.shortcuts import render
from django.views import View
from .models import Post

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "post/post_list.html", {"posts": posts})

class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return JsonResponse({'title': post.title, 'description': post.description, 'author': post.author})

class PostCreateView(View):
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return JsonResponse({'id': post.id, 'title': post.title}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)

class PostDeleteView(View):
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect('/posts/')   