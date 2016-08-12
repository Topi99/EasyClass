from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^nuevo/$', views.Nuevo.as_view(), name="nuevo"),
	url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detail"),
	url(r'^$', views.ListView.as_view(), name="list"),
	url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.ListView.as_view(), name="list_tag"),
]