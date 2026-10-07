from django.urls import path

from . import views


app_name = "app"


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "classes/",
        views.class_list,
        name="class_list",
    ),
    path(
        "classes/add/",
        views.class_create,
        name="class_create",
    ),
    path(
        "classes/<int:pk>/",
        views.class_detail,
        name="class_detail",
    ),
    path(
        "classes/<int:pk>/edit/",
        views.class_update,
        name="class_update",
    ),

    path(
        "trainers/",
        views.trainer_list,
        name="trainer_list",
    ),
    path(
        "trainers/add/",
        views.trainer_create,
        name="trainer_create",
    ),
    path(
        "trainers/<int:pk>/",
        views.trainer_detail,
        name="trainer_detail",
    ),
    path(
        "trainers/<int:pk>/edit/",
        views.trainer_update,
        name="trainer_update",
    ),

    path(
        "schedule/",
        views.schedule_list,
        name="schedule",
    ),
    path(
        "schedule/add/",
        views.schedule_create,
        name="schedule_create",
    ),
]