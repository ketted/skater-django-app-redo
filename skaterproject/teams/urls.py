from django.urls import path
from .views import TeamList, TeamDetail, TeamCreate, TeamUpdate, TeamDelete

urlpatterns = [
    path('', TeamList.as_view(), name='teams-home'),  # rt to /team-index
    path('delete/<int:pk>', TeamDelete.as_view(), name='delete-team'), #rt to teams/delete/pk#
    path('<int:pk>', TeamDetail.as_view(), name='team-detail'), # rt to /skater/pk#
    path('edit/<int:pk>', TeamUpdate.as_view(), name='edit-team'), # rts to /skater/edit/pk#
    path('add', TeamCreate.as_view(), name='add-team'), # rts to skater/add
]