from os import stat
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # url('^$',views.welcome,name='welcome'),
  url('^$',views.news_of_day,name='newsToday'),
  url('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
  url('^search/',views.search_results,name='search_results'),
  url('^article/(\d+)',views.article,name ='article')
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
  