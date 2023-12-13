from django.urls import path
from .views import *

urlpatterns = [
    path('up/',product_upload.as_view()),
    path('dis/',product_view.as_view(),name='view'),
    path('del/<pk>',product_delete.as_view()),
    path('ed/<pk>',product_update.as_view())
]