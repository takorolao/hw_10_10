from django.urls import re_path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    re_path(r'^$', TaskListView.as_view(), name='task-list'),
    re_path(r'^task/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
]
