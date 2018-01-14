from django.conf.urls import url
from . import views

urlpatterns = [
    # /smart/
    url(r'^$', views.IndexView, name='index'),

    # /smart/<node_id>/
    url(r'^(?P<node_id>[0-9]+)/$', views.DetailView, name='detail'),


]