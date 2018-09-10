from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #url(r'', include('touchpoint.urls')),
    url(r'^', include('touchpoint.urls', namespace='touchpoint')),
    #url(r'', include('touchpoint.urls')),
]

