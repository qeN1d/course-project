from django import forms

from .models import Schedule, Trainer, YogaClass


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            "name",
            "bio",
            "experience",
        ]
        widgets = {
            "bio": forms.Textarea(
                attrs={"rows": 5},
            ),
        }


class YogaClassForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = [
            "title",
            "description",
            "duration",
            "level",
            "price",
            "trainer",
            "is_active",
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 5},
            ),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "yoga_class",
            "date",
            "time",
            "places",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"},
            ),
            "time": forms.TimeInput(
                attrs={"type": "time"},
            ),
        }