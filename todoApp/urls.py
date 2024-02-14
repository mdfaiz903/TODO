from . views import home,deleteview,updateview
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('delete-<int:id>/',deleteview,name='deleteview'),
    path('update-<int:id>/',updateview,name='update'),
]
