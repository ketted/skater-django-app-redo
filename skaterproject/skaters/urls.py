from django.urls import path
from .views import SkaterList, SkaterDetail, SkaterDelete, SkaterUpdate, SkaterCreate


urlpatterns = [
    path('', SkaterList.as_view(), name='home'),  # rt to /skater
    path('delete/<int:pk>', SkaterDelete.as_view(), name='delete'), #rt to /skater/delete/pk#
    path('<int:pk>', SkaterDetail.as_view(), name='detail'), # rt to /skater/pk#
    path('edit/<int:pk>', SkaterUpdate.as_view(), name='edit'), # rts to /skater/edit/pk#
    path('add', SkaterCreate.as_view(), name='add'), # rts to skater/add
]