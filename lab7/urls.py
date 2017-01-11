from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^success/?$', views.login_success, name='success'),
    url(r'^service/(?P<id>\d+)$',
        views.ServiceView.as_view(), name='service'),
    url(r'^admin/', admin.site.urls),
]
