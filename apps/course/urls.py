from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), #this is for display
    url(r'new$' , views.new), 
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'destroy/(?P<id>\d+)$', views.destroy)
]                            
