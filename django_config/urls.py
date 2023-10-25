from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_config import settings
from app.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', IndexView.as_view(), name = 'index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
