from django.urls import reverse_lazy
from django.views import generic

from tracker.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tracker:tag-list")
    template_name = "tracker/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tracker:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tracker:tag-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
