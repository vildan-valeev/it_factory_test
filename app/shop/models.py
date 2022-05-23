from django.db import models
import uuid



class UUIDModel(models.Model):
    """Abstract model with `uuid` id as primary key."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, editable=False, null=True, verbose_name='Обновлен')

    class Meta:
        abstract = True


class Employee(UUIDModel):
    """Работник"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    phone = models.CharField(verbose_name="Номер телефона", max_length=255)

    class Meta:
        verbose_name = "Работника"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.name


class Market(UUIDModel):
    """Работник"""
    name = models.CharField(verbose_name="Название", max_length=255, null=False, )
    employee = models.ForeignKey(Employee, verbose_name="Работник", on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name


class Visit(UUIDModel):
    """Работник"""
    market = models.ForeignKey(Market, verbose_name="Работник", on_delete=models.PROTECT, null=False, blank=False)
    latitude = models.FloatField(verbose_name="Широта", null=False, blank=False)
    longitude = models.FloatField(verbose_name="Долгота", null=False, blank=False)
    visit_date = models.DateTimeField(verbose_name="Время посещения", auto_now_add=True, )

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f"{self.id} {self.market.employee.name} {self.market.name}"
