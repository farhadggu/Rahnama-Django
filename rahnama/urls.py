#Library Import
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.utils.translation import gettext_lazy as _
#Local Import
from post.views import change_lang


urlpatterns = [
    path('change_lang', change_lang, name="change_lang"),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('post.urls', namespace='posts')),
    prefix_default_language=False,
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)