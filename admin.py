from django.contrib import admin

from .models import Schedule, Trainer, YogaClass


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["name", "experience"]
    search_fields = ["name"]


@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "level",
        "duration",
        "price",
        "trainer",
        "is_active",
    ]
    list_filter = ["level", "is_active"]
    search_fields = ["title", "description"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "yoga_class",
        "date",
        "time",
        "places",
    ]
    list_filter = ["date"]