from . views import home,deleteview
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('delete-<int:id>/',deleteview,name='deleteview'),
]
