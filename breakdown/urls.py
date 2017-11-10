from django.conf.urls import url
from breakdown.views import *
from django.views.generic import TemplateView

from . import views
app_name = 'breakdown'
urlpatterns=[
  # url(r'^$', TemplateView.as_view(template_name="info.html")),
    url(r'^$',views.addbreakdownlogin, name = 'BDlogin'),
    url(r'^d/$',views.addbreakdownResult,name = 'BDResult'),
    url(r'^loglist/$',views.showbreakdownlogin_list, name = 'LoginList'),
    url(r'^loglist/(?P<pk>\w+)/u/$',views.updatebreakdownlogin_list, name = 'LoginListUpdate'),
    url(r'^loglist/(?P<pk>\w+)/$',views.updatebreakdownlogin, name = 'LoginListUpdateShow'),
    url(r'^loglist/(?P<pk>\w+)/d/$',views.delectbreakdownlist, name = 'DelectLogList'),
]