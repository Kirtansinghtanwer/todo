from django.urls import path
from . import views

urlpatterns = [
    path("addTask/",views.addTask,name = 'addTask'),
    path("markasdone/<int:pk>/",views.mark_as_done,name = "markasdone"),
    path("markasundone/<int:pk>/",views.mark_as_undone,name = "markasundone"),
    path("updatetask/<int:pk>/",views.update_Task,name = "update_Task"),
    path("delettask/<int:pk>/",views.delet_Task,name = "delet_Task"),
]