from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    
    # login / logout urls
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    
    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

]
