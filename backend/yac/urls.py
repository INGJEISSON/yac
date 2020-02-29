"""
  yac URL Configuration

"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views import CustomObtainAuthToken

schema_view = get_swagger_view(title='API ConserBI')
router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    # statics and media
    url(r'^documents/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),

    # API REST FRAMEWORK
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-docs/', schema_view),
    path('api/', include('api.urls')),

    url(r'^api-token-auth/', CustomObtainAuthToken.as_view())


]
