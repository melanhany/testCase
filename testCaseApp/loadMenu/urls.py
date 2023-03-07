from django.urls import path
from loadMenu.views import IndexView, IndexDetail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('men/', IndexDetail.as_view(), name='index'),
    path('women/', IndexDetail.as_view(), name='index'),
    path('men/<str:name>/', IndexView.as_view(), name='index'),
    path('women/<str:name>/', IndexView.as_view(), name='index')
]
