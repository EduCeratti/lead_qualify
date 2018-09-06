# from django.conf.urls import patterns, url

# from touchpoint.views import HomePageView

# urlpatterns = patterns(
#     '',

#     url(r'^$', HomePageView.as_view(), name='home'),
# )

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from touchpoint import views
 
urlpatterns = [
    url(r'^touchpoint/$', views.TouchpointList.as_view(), name='touchpoint-list'),
    url(r'^touchpoint/(?P<pk>[0-9]+)/$', views.TouchpointDetail.as_view(), name='touchpoint-detail'),
    #url(r'^touchpoint/(?P<username>[]+)/$', views.TouchpointDetail.as_view(), name='touchpoint-detail'),
]