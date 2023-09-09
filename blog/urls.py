from django.urls import path

from blog.views import BlogView, BlogDetailView, SearchbarView

app_name = 'blog'

DAY = 24 * 60 * 60

urlpatterns = [
    # path('blog/', cache_page(DAY)(BlogView.as_view()), name='blog'),
    # path('<slug:slug>/', cache_page(DAY)(BlogView.as_view()), name='post_with_category'),
    # path('blog-details/', cache_page(DAY)(BlogDetailView.as_view()), name='blog_details'),


    path('', BlogView.as_view(), name='index'),
    path('search/', SearchbarView.as_view(), name='search'),
    path('category/<slug:category_slug>/', BlogView.as_view(), name='post_with_category'),
    path('tag/<slug:tag_slug>/', BlogView.as_view(), name='post_with_tag'),
    path('blog-details/<slug:post_slug>/', BlogDetailView.as_view(), name='blog_details'),

]
