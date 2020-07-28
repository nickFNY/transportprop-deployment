from django.conf.urls import url
from basic_app import views
from .views import contactView



urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^team/$',views.TeamView.as_view(),name='team'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    # url(r'^contact/$',views.ContactView.as_view(),name='contact'),
    url(r'^properties/$',views.PropertyListView.as_view(),name='properties'),
    url(r'^contact/$',views.contactView,name='contact'),
    url(r'^news/$',views.NewsListView.as_view(),name='news'),
    url(r'^news/(?P<pk>\d+)$',views.NewsDetailView.as_view(),name='news_detail'),
]




# urlpatterns = [
#     url(r'^$',views.HomeView.as_view(),name='home'),
#     url(r'^team/$',views.TeamView.as_view(),name='team'),
#     url(r'^contact/$',views.ContactView.as_view(),name='contact'),
#     url(r'^properties/$',views.PropertyListView.as_view(),name='properties')
# ]
