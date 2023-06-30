from django import forms
from django.db import models

from ess.utils import format_phone

class PhoneField(models.CharField):
    """Поле для хранения телефонного номера."""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        return format_phone(value)

    def formfield(self, **kwargs):
        return super().formfield(max_length=20, **kwargs)


class MultiLineCharField(models.CharField):
    """Поле для коротких многострочных текстовых данных."""

    def formfield(self, **kwargs):
        kwargs["widget"] = forms.Textarea
        return super().formfield(**kwargs)


class TimeField(models.TimeField):
    """Поле для указания времени в формате XX:XX."""

    def formfield(self, **kwargs):
        kwargs["widget"] = forms.TimeInput(attrs={"type":"time","size":5})
        return super().formfield(**kwargs)