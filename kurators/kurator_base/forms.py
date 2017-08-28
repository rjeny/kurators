from django import forms
from .models import CurTimeResult


class CurResultForm (forms.ModelForm):
    class Meta:
        model = CurTimeResult
        fields = "__all__"
        widgets = {
            "cur_time": forms.HiddenInput,
            "group": forms.HiddenInput,
            "date": forms.TextInput(attrs={
                "class": "datepicker",
                "data-date-format": "dd.mm.yyyy"
            }),
            "cur_rating": forms.HiddenInput,
            "group_rating": forms.HiddenInput
        }
        labels = {
            "date": "Дата проведения",
            "problems": "Проблемы, которые возникли",
            "plus": "Что было круто",
            "emotions": "Расскажи как ТЫ себя чувствуешь, распиши свои эмоции в эту коробочку для текста :D",
            "comments": "Комментарии студентов",
        }
