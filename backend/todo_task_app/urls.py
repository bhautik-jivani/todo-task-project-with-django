# ========== django libraries import ==========
from django.urls import path

# ========== project views libraries import =========
from todo_task_app import views

urlpatterns = [
    path(
        "",
        views.TodoTaskViewSet.as_view({"get": "list", "post": "create"}),
        name="todo_task_listorcreate_api",
    ),
    path(
        "<int:id>/",
        views.TodoTaskViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="todo_task_listorcreate_api",
    ),
]
