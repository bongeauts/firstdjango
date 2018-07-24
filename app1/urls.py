
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^boxes/$', views.BoxList.as_view(), name='boxes')
    url(r'^boxes/(?P<pk>\d+)/$', views.BoxList.as_view(), name='box_pk')

]

urlpatterns = format_suffix_patterns(urlpatterns)
