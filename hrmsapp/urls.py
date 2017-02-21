from django.conf.urls import patterns,url
from django.views.generic.dates import ArchiveIndexView
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views
from .models import Archive
from hrmsapp.views import ArchiveMonthArchiveView

#from .import views
'''
urlpatterns = patterns('',
    url(r'^login/$',auth_views.login,name='login',kwargs={'template_name':'hrmsapp/login.html'}),
    url(r'^logout/$',auth_views.logout,name='logout',kwargs={'name':'/'}),
    url(r'^password_change$',auth_views.password_change,name='password_change',kwargs={'template_name': 'hrmsapp/password_change_form.html','post_change_redirect':'hrmsapp:password_change_done',}),
    url(r'^password_change_done$',auth_views.password_change_done,name='password_change_done',kwargs={'template_name': 'hrmsapp/password_change_done.html'}),
    
)
'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('hrmsapp.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'}),
    url(r'^archive/$',ArchiveIndexView.as_view(model=Archive,date_field="pub_date"),name="archive"), 
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',ArchiveMonthArchiveView.as_view(),name="archive_month"),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ArchiveMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),


]


