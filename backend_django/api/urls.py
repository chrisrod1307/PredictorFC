from django.urls import path
from .views import predict_match

urlpatterns = [
    path('predict/', predict_match),
]