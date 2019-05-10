from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^get_data', views.get_data, name='get_data'),
    url(r'^$', views.select_data, name='select_data'),
]
