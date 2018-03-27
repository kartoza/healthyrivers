# coding=utf-8

from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from base.api_views.location_site import (
    LocationSiteList,
    LocationSiteDetail,
)


api_urls = [
    url(r'^api/location-site/$', LocationSiteList.as_view()),
    url(r'^api/location-site/(?P<pk>[0-9]+)/$',
        LocationSiteDetail.as_view()),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing_page.html")),
    url(r'^api/docs/', include_docs_urls(title='Healthyrivers API'))
] + api_urls
