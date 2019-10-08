from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import static
from django.views.static import serve

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import settings
from Appis import views as appis

# REST
router = routers.DefaultRouter()
router.register('order', appis.OrderViewSet)
router.register('member', appis.MemberViewSet)

# URL
urlpatterns = [    
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$',  serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_DIR}),

    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='微信小程序')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
