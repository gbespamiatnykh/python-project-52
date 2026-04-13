from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("name")
        )
    description = models.TextField(blank=True, verbose_name=_("description"))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name=_("status"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_tasks",
        verbose_name=_("executor"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="assigned_tasks",
        verbose_name=_("author"),
    )
    labels = models.ManyToManyField(
        Label,
        related_name="tasks",
        verbose_name=_("labels"),
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = _("task")
