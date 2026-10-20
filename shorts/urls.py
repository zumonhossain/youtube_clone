from django.urls import path

from shorts.views import ShortsView, ShortsWatchView, ShortsMusicView

urlpatterns = [
    path('', ShortsView.as_view(), name='shorts'),
    path('watch/', ShortsWatchView.as_view(), name='watch'),
    path('music/', ShortsMusicView.as_view(), name='music'),
]



