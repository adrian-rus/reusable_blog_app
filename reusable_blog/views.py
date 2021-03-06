from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def post_list(request):
    # creating a view that will return a list of Posts
    # that were published prior to 'now' and
    # render them to the 'blogposts.html' template
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, 'reusable_blog/blogposts.html',
                  {'posts': posts})


def post_detail(request, id):
    # creating a view that will return a single
    # Post object based on the Post id and then
    # render it to the 'postdetail.html' template
    # return a 404 error if the post is not found
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'reusable_blog/postdetail.html',
                  {'post': post})


def new_post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm()
        return render(request, 'reusable_blog/blogpostform.html',
                      {'form': form})
    else:
        return render(request, 'reusable_blog/blogpostform.html',
                      {'form': form})






