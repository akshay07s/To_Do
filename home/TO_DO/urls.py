from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.to_do , name='to_do'),
]