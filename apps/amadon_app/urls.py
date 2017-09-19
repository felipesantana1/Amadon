from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^checkout$', views.checkout),
    url(r'^goback$', views.goBack)

]