from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property

from ess.models.fields import PhoneField

class User(AbstractUser):
    email = models.EmailField("E-mail", unique=True)
    phone = PhoneField("Телефон", blank=True)

    class Meta:
        db_table = "users"
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username

    # @cached_property
    # def cities(self):
    #     return self.city.only("pk", "title", "label")

    # @cached_property
    # def cities_index(self):
    #     return tuple(self.cities.values_list("pk", flat=True))

    # @cached_property
    # def has_multi_city(self):
    #     return len(self.cities_index) > 1

    # def city_filter(self, queryset):
    #     # if self.is_superuser:
    #     #     return queryset
    #     return queryset.filter(city__in=self.cities_index)
