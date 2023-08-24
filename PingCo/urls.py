from django.urls import path

from .views import (IndexView, AboutView, MissionView, ContactView, TeamView, RoadMapView,
                    AssetView)

from django.views.decorators.cache import cache_page

app_name = 'PingCo'

DAY = 24 * 60 * 60

urlpatterns = [
    # path('', cache_page(DAY)(IndexView.as_view()), name='index'),
    # path('about/', cache_page(DAY)(AboutView.as_view()), name='about'),
    # path('vision_mission/', cache_page(DAY)(MissionView.as_view()), name='mission'),
    # path('contact/', cache_page(DAY)(ContactView.as_view()), name='contact'),
    # path('team/', cache_page(DAY)(TeamView.as_view()), name='team'),
    # path('roadmap/', cache_page(DAY)(RoadMapView.as_view()), name='roadmap'),
    # path('parti-assets/', cache_page(DAY)(AssetView.as_view()), name='parti_assets'),

    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('vision_mission/', MissionView.as_view(), name='mission'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('team/', TeamView.as_view(), name='team'),
    path('roadmap/', RoadMapView.as_view(), name='roadmap'),
    path('parti-assets/', AssetView.as_view(), name='parti_assets'),

]
