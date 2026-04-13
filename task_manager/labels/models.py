from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ValidationError
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        verbose_name = _("label")
