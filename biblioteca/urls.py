from django.urls import include,re_path
from . import views

urlpatterns = [
    re_path(r'^biblioteca/$', views.JSONResponse.prestamo_list),
    re_path(r'^biblioteca/(?P<pk>[0-9]+)/$', views.JSONResponse.prestamo_detail),
]
