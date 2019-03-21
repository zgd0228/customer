from django.contrib import admin

from django.conf.urls import url
from web import views


urlpatterns = [

    url(r'^customer/list/$',views.customer_list,name='customer_list'),
    url(r'^customer/add/$',views.customer_add,name='customer_add'),
    url(r'^login/$',views.login,name='login'),
    url(r'^pay/list/$',views.payment_list,name='pay_list'),
    url(r'^pay/add/$',views.payment_add,name='pay_add'),
    url(r'^customer/delete/(?P<cid>\d+)/$',views.customer_delete,name='customer_delete'),
    url(r'^customer/edit/(?P<cid>\d+)/$',views.customer_edit,name='customer_edit'),
    url(r'^pay/delete/(?P<cid>\d+)/$',views.pay_delete,name='pay_delete'),
    url(r'^pay/edit/(?P<cid>\d+)/$',views.pay_edit,name='pay_edit'),
]
