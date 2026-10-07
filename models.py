from django.db import models
from django.urls import reverse


class Trainer(models.Model):
    name = models.CharField(
        "Имя тренера",
        max_length=150,
    )
    bio = models.TextField(
        "Описание",
        blank=True,
    )
    experience = models.PositiveIntegerField(
        "Опыт работы, лет",
        default=0,
    )

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "app:trainer_detail",
            kwargs={"pk": self.pk},
        )


class YogaClass(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Начальный"),
        ("middle", "Средний"),
        ("advanced", "Продвинутый"),
    ]

    title = models.CharField(
        "Название занятия",
        max_length=150,
    )
    description = models.TextField(
        "Описание",
    )
    duration = models.PositiveIntegerField(
        "Продолжительность, минут",
        default=60,
    )
    level = models.CharField(
        "Уровень",
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner",
    )
    price = models.DecimalField(
        "Стоимость",
        max_digits=8,
        decimal_places=2,
    )
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="classes",
        verbose_name="Тренер",
    )
    is_active = models.BooleanField(
        "Активно",
        default=True,
    )

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "app:class_detail",
            kwargs={"pk": self.pk},
        )


class Schedule(models.Model):
    yoga_class = models.ForeignKey(
        YogaClass,
        on_delete=models.CASCADE,
        related_name="schedule",
        verbose_name="Занятие",
    )
    date = models.DateField("Дата")
    time = models.TimeField("Время")
    places = models.PositiveIntegerField(
        "Количество мест",
        default=10,
    )

    class Meta:
        verbose_name = "Занятие в расписании"
        verbose_name_plural = "Расписание"
        ordering = ["date", "time"]

    def __str__(self):
        return (
            f"{self.yoga_class.title} — "
            f"{self.date} {self.time}"
        )