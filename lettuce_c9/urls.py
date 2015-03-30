from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import quick_test
from blog.views import test1
from blog.views import test2
from blog.views import test3

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lettuce_c9.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quick-test/$', quick_test),
    url(r'^blog1/$', test1),
    url(r'^blog2/$', test2),
    url(r'^blog3/$', test3),
)
