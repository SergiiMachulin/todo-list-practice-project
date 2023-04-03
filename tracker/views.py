from django.views import generic

from tracker.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
