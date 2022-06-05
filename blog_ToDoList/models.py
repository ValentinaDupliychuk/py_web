from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Note(models.Model):

    class Ratings(models.IntegerChoices):
        ACTIVE = 0, _('Активно')
        POSTPONED = 1, _('Отложено')
        COMPlETED = 3, _('Выполнено')

    title = models.CharField(max_length=300, verbose_name=_("Название записи"))
    message = models.TextField(default='', verbose_name=_("Сообщение"))
    public = models.BooleanField(default=True, verbose_name=_("Опубликовано"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Время создания"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Автор"))
    significance = models.BooleanField(default=False, verbose_name=_("Важность"))
    rating = models.IntegerField(default=Ratings.ACTIVE, choices=Ratings.choices, verbose_name=_('Статус'))

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = _("запись")
        verbose_name_plural = _("записи")


