# ========== rest_framework libraries import ==========
from rest_framework import serializers

# ========== project models libraries import =========
from todo_task_app.models import TodoTask


class TodoTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = ["id", "name", "description", "status", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "description": {"required": True, "allow_blank": False},
            "status": {
                "default": False,
            },
        }
