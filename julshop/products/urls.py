from django.conf.urls import url, include
from django.contrib import admin
from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),

    # url(r'^$', views.ProductList, name='ProductList'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    # url(r'^landing/', views.landing, name='landing'),
]