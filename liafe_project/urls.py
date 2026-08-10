from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve as serve_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('messages_app.urls')),
    # Custom pages — must be LAST to avoid swallowing other patterns
    path('pages/', include('pages.urls')),
]

# django.conf.urls.static.static() silently returns no routes when DEBUG=False,
# which would 404 every dashboard-uploaded image in production. Serve explicitly
# instead — harmless when Cloudinary is configured, since ImageField.url then
# points at Cloudinary's CDN and this route is simply never hit.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve_static, {'document_root': settings.MEDIA_ROOT}),
]
