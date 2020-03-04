from django.conf.urls import url
from django.urls import path,re_path
from .views import DocumentView,DocumentListView

urlpatterns = [

    path(r'document/',DocumentView.as_view(),name='DocumentView'),
    path(r'documentlist/',DocumentListView.as_view(),name='DocumentListView')

]