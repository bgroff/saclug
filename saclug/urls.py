from polls.views import PollView, ResultsView, PollIndexView

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(
        regex=r'^$',
        view=PollIndexView.as_view(),
        name='index'
    ),

    url(
        regex=r'^(?P<poll_id>\d+)/vote/$',
        view=PollView.as_view(),
        name='vote'
    ),

    url(
        regex=r'^(?P<poll_id>\d+)/results/$',
        view=ResultsView.as_view(),
        name='results'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
