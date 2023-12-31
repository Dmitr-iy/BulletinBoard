from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('debug/', include('debug_toolbar.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
