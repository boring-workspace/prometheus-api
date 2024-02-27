from django.urls import path

from . import views

urlpatterns = [
    path("stream", views.sse_stream, name="sse_stream"),
    path("ohlc", views.ohlc, name="ohlc"),
    path("sse", views.sse, name="sse"),
]
