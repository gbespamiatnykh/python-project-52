import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Label, Task


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name="labels",
        label=_("Label"),
        lookup_expr="exact",
    )
    author = django_filters.BooleanFilter(
        field_name="author",
        method="filter_my_tasks",
        label=_("Only your tasks"),
        widget=forms.CheckboxInput,
    )

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels", "author"]
