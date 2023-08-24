from django.views.generic import TemplateView

from django.core.paginator import Paginator
from blog.models import Post
from common.views import CommonContextMixin, CommonFormsMixin, BlogContextMixin


class BlogView(CommonContextMixin, BlogContextMixin, CommonFormsMixin, TemplateView):  # feedback
    template_name = 'blog/blog.html'
    title = 'PingCo - Блог'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.order_by('-published_at')

        category_id = self.kwargs.get('category_id')
        tag_id = self.kwargs.get('tag_id')

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if tag_id:
            queryset = queryset.filter(tag__id=tag_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['blog'] = 'current-item'
        context['blog_view'] = 'index'

        paginator = Paginator(self.get_queryset(), self.paginate_by)

        page = self.request.GET.get('page')
        posts_paginator = paginator.get_page(page)

        context['posts'] = posts_paginator
        return context


class BlogDetailView(CommonContextMixin, BlogContextMixin, CommonFormsMixin, TemplateView):  # feedback
    template_name = 'blog/blog-details.html'
    title = 'PingCo - Blog-details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_slug = self.kwargs.get('post_slug')
        post = Post.objects.get(slug=post_slug)
        context['post'] = post
        context['blog_detail'] = 'current-item'
        context['blog_detail_view'] = 'blog_details'
        return context
