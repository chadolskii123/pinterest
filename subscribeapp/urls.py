from django.urls import path

from subscribeapp.views import SubscribeView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns=[
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),

]