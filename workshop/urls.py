from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
