from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PingCo.urls', namespace='PingCo')),
    path('blog/', include('blog.urls', namespace='blog')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
