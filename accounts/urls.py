from django.conf.urls import url
from django.contrib.auth.views import logout, logout_then_login, login
from . import views

urlpatterns = [
	url(r'^registro/', views.Registration.as_view(), name="registro"),
	url(r'^complete-profile/', views.CompleteProfile.as_view(), name="complete-reg"),
	url(r'^profile/$', views.Dashboard.as_view(), name="perfil"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),
]
