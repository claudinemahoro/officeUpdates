from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^department/(\d+)', views.my_office, name='office'),
    url(r'^department/(\d+)/join/$', views.join, name='join'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^new/post$', views.new_post, name='new-post')
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)