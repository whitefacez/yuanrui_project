from django.conf.urls import url
from breakdown.views import addbreakdownlogin,addbreakdownResult,showbreakdownlogin_list
from django.views.generic import TemplateView

from . import views
app_name = 'breakdown'
urlpatterns=[
  # url(r'^$', TemplateView.as_view(template_name="info.html")),
    url(r'^$',views.addbreakdownlogin,name = 'BDlogin'),
    
    url(r'^d/$',views.addbreakdownResult,name = 'BDResult'),
    url(r'^loglist/$',views.showbreakdownlogin_list,name = 'login_list'),
    url(r'^loglist/(?P<pk>\d+)/u/$',views.updatebreakdownlogin_list,name = 'login_list_update'),
]