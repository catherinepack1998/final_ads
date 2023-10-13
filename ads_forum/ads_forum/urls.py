from django.contrib import admin
from django.urls import include, path
#from django.conf.urls.static import static

#from ads_forum.ads_forum import settings


urlpatterns = [
    path('', include('appl.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('ads/', include('appl.urls')),
    path('debug/', include("debug_toolbar.urls")),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

