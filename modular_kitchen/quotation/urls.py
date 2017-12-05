from django.conf.urls import include, url
import quotation.views as views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^form/', views.Form.as_view(), name='form'),

]
