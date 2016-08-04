from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as UrlsPost
from accounts import urls as UrlsAccounts
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include(UrlsPost, namespace="posts")),
    url(r'^accounts/', include(UrlsAccounts)),
    url('', include('social.apps.django_app.urls', namespace="social")),
    url(
    		r'^media/(?P<path>.*)$',
    		serve, 
    		{'document_root':settings.MEDIA_ROOT}
    ),
]
