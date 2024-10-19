# ========== django libraries import ==========
from django.core.cache import cache

# ========== rest_framework libraries import ==========
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# ========== project serializers libraries import =========
from todo_task_app.serializers import TodoTaskSerializer

# ========== project models libraries import =========
from todo_task_app.models import TodoTask


# Create your views here.
class TodoTaskViewSet(ModelViewSet):
    serializer_class = TodoTaskSerializer
    queryset = TodoTask.objects.all()
    lookup_field = "id"
    cache_key = "todo_tasks"

    def list(self, request, *args, **kwargs):
        serialized_data = cache.get(self.cache_key)
        if not serialized_data:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            serialized_data = serializer.data
            cache.set(
                self.cache_key, serialized_data, timeout=60 * 15
            )  # Cache for 15 minutes
        return Response(serialized_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(self.cache_key)  # Clear cache after creation
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(self.cache_key)  # Clear cache after update
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        cache.delete(self.cache_key)  # Clear cache after update
        return Response(
            {"message": "Todo Task deleted successfull!"}, status=status.HTTP_200_OK
        )
