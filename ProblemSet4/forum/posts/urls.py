from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('add/',views.add, name='add'),
    path('entry/<int:post_id>/',views.get_entry,name='get_entry')
]