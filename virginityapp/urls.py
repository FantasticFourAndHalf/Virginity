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
]