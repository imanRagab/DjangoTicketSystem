from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^all/$', views.all_tickets_view),
    url(r'^add/$', views.add_ticket_view),
    url(r'^edit/(?P<ticket_id>[0-9]+)/$', views.change_status_view),
]