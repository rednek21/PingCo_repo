from django.urls import path, include

from .views import (IndexView, AboutView, MissionView, BlogView, ContactView, TeamView, RoadMapView,
                    AssetView, BlogDetailView)

from django.views.decorators.cache import cache_page

app_name = 'PingCo'

urlpatterns = [
    # path('', cache_page(86400)(IndexView.as_view()), name='index'),
    # path('about/', cache_page(86400)(AboutView.as_view()), name='about'),
    # path('vision_mission/', cache_page(86400)(MissionView.as_view()), name='mission'),
    # path('blog/', cache_page(86400)(BlogView.as_view()), name='blog'),
    # path('contact/', cache_page(86400)(ContactView.as_view()), name='contact'),
    # path('team/', cache_page(86400)(TeamView.as_view()), name='team'),
    # path('roadmap/', cache_page(86400)(RoadMapView.as_view()), name='roadmap'),
    # path('parti-assets/', cache_page(86400)(AssetView.as_view()), name='parti_assets'),
    # path('blog-details/', cache_page(86400)(BlogDetailView.as_view()), name='blog_details'),

    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('vision_mission/', MissionView.as_view(), name='mission'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('team/', TeamView.as_view(), name='team'),
    path('roadmap/', RoadMapView.as_view(), name='roadmap'),
    path('parti-assets/', AssetView.as_view(), name='parti_assets'),
    path('blog-details/', BlogDetailView.as_view(), name='blog_details'),

]
