from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('dictvalue/', views.dictvalue, name='dictvalue'),
    path('getdata', views.getdata, name='getdata'),
    path('postdata', views.getpostdata, name='postdata'),
    path('update/<int:pk>', views.display, name='update'),
    path('get_post_api', views.get_post_api, name='postdata'),
    path('get_put_delete_api/<int:pk>', views.get_put_delete_api, name='get_put_delete_api'),
    path('get_post_apiview', views.get_post_apiview.as_view(), name='get_post_apiview'),
    path('get_put_delete_apiview/<int:id>', views.get_put_delete_apiview.as_view(), name='get_put_delete_apiview'),
    path('1/', views.get_post_genericapiView.as_view(), name='get_post_apiview'),
    path('2/', views.get_put_delete_genericapiView.as_view(), name='get_put_delete_apiview'),
    path('3/', views.AuthView.as_view(), name='get_put_delete_apiview'),
]
