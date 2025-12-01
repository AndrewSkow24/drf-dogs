from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(verbose_name="описание", null=True, blank=True)

    def __str__(self):
        return f"Breed: {self.name}"

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(max_length=255, verbose_name="кличка")
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    breed = models.ForeignKey(
        Breed, on_delete=models.SET_NULL, verbose_name="порода", blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="dogs/photo", verbose_name="фото", null=True, blank=True
    )
    date_born = models.DateField(verbose_name="дата рождения", blank=True, null=True)

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return f"Dog: {self.name}"
