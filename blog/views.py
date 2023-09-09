from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.paginator import Paginator

from blog.forms import SearchbarForm
from blog.models import Post
from common.views import CommonContextMixin, CommonFormsMixin, BlogContextMixin


class BlogView(CommonContextMixin, BlogContextMixin, CommonFormsMixin, TemplateView):  # feedback
    template_name = 'blog/blog.html'
    title = 'PingCo - Блог'
    paginate_by = 1

    def get_queryset(self):
        queryset = Post.objects.order_by('-published_at')

        category_slug = self.kwargs.get('category_slug')
        tag_slug = self.kwargs.get('tag_slug')

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if tag_slug:
            queryset = queryset.filter(tag__slug=tag_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['blog'] = 'current-item'
        context['blog_view'] = 'index'

        paginator = Paginator(self.get_queryset(), self.paginate_by)

        page = self.request.GET.get('page')
        posts_paginator = paginator.get_page(page)

        context['posts'] = posts_paginator
        context['searchform'] = SearchbarForm()
        return context


class SearchbarView(BlogView):
    template_name = 'blog/searchbar.html'
    posts_qs = None

    def get(self, request, *args, **kwargs):
        form = SearchbarForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['title']
            posts = Post.objects.filter(title__icontains=query).order_by('-published_at')
            self.posts_qs = posts

        context = self.get_context_data()
        paginator = Paginator(self.posts_qs, self.paginate_by)

        page = self.request.GET.get('page')
        posts_paginator = paginator.get_page(page)

        context['found'] = posts_paginator
        context['searchform'] = form
        return render(request, self.template_name, context)


class BlogDetailView(CommonContextMixin, BlogContextMixin, CommonFormsMixin, TemplateView):  # feedback
    template_name = 'blog/blog-details.html'
    title = 'PingCo - Blog-details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_slug = self.kwargs.get('post_slug')
        post = Post.objects.get(slug=post_slug)
        context['post'] = post

        all_posts = Post.objects.order_by('-published_at')

        current_post_index = -1
        for i, p in enumerate(all_posts):
            if p.id == post.id:
                current_post_index = i
                break

        previous_post = all_posts[current_post_index + 1] if current_post_index < len(all_posts) - 1 else all_posts[0]
        next_post = all_posts[current_post_index - 1] if current_post_index > 0 else all_posts[len(all_posts) - 1]

        context['prev'] = previous_post
        context['next'] = next_post

        context['blog_detail'] = 'current-item'
        context['blog_detail_view'] = 'blog_details'
        context['searchform'] = SearchbarForm()
        return context

