from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ScheduleForm, TrainerForm, YogaClassForm
from .models import Schedule, Trainer, YogaClass


def home(request):
    return render(request, "app/home.html")
    classes = YogaClass.objects.filter(
        is_active=True,
    )[:3]
    trainers = Trainer.objects.all()[:3]
    schedule = Schedule.objects.select_related(
        "yoga_class",
    ).order_by("date", "time")[:5]

    return render(
        request,
        "studio/home.html",
        {
            "classes": classes,
            "trainers": trainers,
            "schedule": schedule,
        },
    )


def class_list(request):
    classes = YogaClass.objects.filter(
        is_active=True,
    )
    return render(
        request,
        "studio/class_list.html",
        {"classes": classes},
    )


def class_detail(request, pk):
    yoga_class = get_object_or_404(YogaClass, pk=pk)
    schedule = yoga_class.schedule.all()

    return render(
        request,
        "studio/class_detail.html",
        {
            "yoga_class": yoga_class,
            "schedule": schedule,
        },
    )


def class_create(request):
    if request.method == "POST":
        form = YogaClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Занятие успешно добавлено.",
            )
            return redirect("studio:class_list")
    else:
        form = YogaClassForm()

    return render(
        request,
        "studio/form.html",
        {
            "form": form,
            "title": "Добавить занятие",
        },
    )


def class_update(request, pk):
    yoga_class = get_object_or_404(YogaClass, pk=pk)

    if request.method == "POST":
        form = YogaClassForm(
            request.POST,
            request.FILES,
            instance=yoga_class,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Занятие изменено.",
            )
            return redirect(
                "studio:class_detail",
                pk=yoga_class.pk,
            )
    else:
        form = YogaClassForm(instance=yoga_class)

    return render(
        request,
        "studio/form.html",
        {
            "form": form,
            "title": "Редактировать занятие",
        },
    )


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(
        request,
        "studio/trainer_list.html",
        {"trainers": trainers},
    )


def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    classes = trainer.classes.filter(is_active=True)

    return render(
        request,
        "studio/trainer_detail.html",
        {
            "trainer": trainer,
            "classes": classes,
        },
    )


def trainer_create(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Тренер успешно добавлен.",
            )
            return redirect("studio:trainer_list")
    else:
        form = TrainerForm()

    return render(
        request,
        "studio/form.html",
        {
            "form": form,
            "title": "Добавить тренера",
        },
    )


def trainer_update(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)

    if request.method == "POST":
        form = TrainerForm(
            request.POST,
            request.FILES,
            instance=trainer,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Данные тренера изменены.",
            )
            return redirect(
                "studio:trainer_detail",
                pk=trainer.pk,
            )
    else:
        form = TrainerForm(instance=trainer)

    return render(
        request,
        "studio/form.html",
        {
            "form": form,
            "title": "Редактировать тренера",
        },
    )


def schedule_list(request):
    schedule = Schedule.objects.select_related(
        "yoga_class",
        "yoga_class__trainer",
    )

    return render(
        request,
        "studio/schedule.html",
        {"schedule": schedule},
    )


def schedule_create(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Занятие добавлено в расписание.",
            )
            return redirect("studio:schedule")
    else:
        form = ScheduleForm()

    return render(
        request,
        "studio/form.html",
        {
            "form": form,
            "title": "Добавить в расписание",
        },
    )