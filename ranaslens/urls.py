from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "RANA'S LENS"
admin.site.index_title = 'Admin Dashboard'

urlpatterns = [
    path("", include("lens.urls")),
    path('admin/', admin.site.urls),
] 

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handling404 = 'lens.views.handling404'
