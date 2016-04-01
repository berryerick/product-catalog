from django.conf.urls import url, include
from . import views

urlpatterns = [
    
    url(r'^/(?P<product_id>\d+)/$', views.product, name = 'product'),
    url(r'^$', views.index, name = 'index'),
]

