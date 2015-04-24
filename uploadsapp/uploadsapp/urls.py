from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homework/', include('homework.urls', namespace="homework")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)