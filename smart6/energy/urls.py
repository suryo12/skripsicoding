from django.conf.urls import url, include
from . import views
from .views import APINodeView

app_name = 'energy'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', APINodeView.as_view(), name='APINodeView'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]