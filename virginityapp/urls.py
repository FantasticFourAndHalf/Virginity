# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 06.09.2017


from django.conf.urls import url

from virginityapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^phone/', views.phone_request),
    url(r'^menu/', views.menu),
    url(r'^dish/(?P<dish_id>[0-9]+)', views.dish),
    url(r'^basket/', views.basket),


    url(r'^cart/(?P<dish_id>[0-9]+)', views.add_to_cart),
    url(r'^cart/delete/(?P<item_id>[0-9]+)', views.delete_from_cart),
    url(r'^cart/amount/(?P<item_id>[0-9]+)/(?P<amount>[0-9]+)', views.change_cart_amount),
    url(r'^user/', views.user),

    url(r'^order/(?P<order_id>[0-9]+)', views.order),
    url(r'^order/', views.make_order),
]