from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^list/','BookDB.views.index',name="BookDB_list"),
                       url(r'^search/$','BookDB.views.Search',name="BookDB_search"),
                       url(r'^none/$','BookDB.views.none',name="BookDB_none"),
                       url(r'^bookauthor/$','BookDB.views.bookauthor',name = "BookDB_bookauther"),
                       url(r'^update-id=(?P<id>\d+)/$', 'BookDB.views.update',name="BookDB_update"),
                       url(r'^delete-id=(?P<id>\d+)/$', 'BookDB.views.delete',name="BookDB_delete"),
                       url(r'^beforeadd/','BookDB.views.beforeadd',name='BookDB_beforeadd'),
                       url(r'^add/','BookDB.views.add',name='BookDB_add'),
                       url(r'^addauth/','BookDB.views.addauth',name='BookDB_addauth'),
                       url(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name="media"),
    # Examples:
    # url(r'^$', 'lab3.views.home', name='home'),
    # url(r'^lab3/', include('lab3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
