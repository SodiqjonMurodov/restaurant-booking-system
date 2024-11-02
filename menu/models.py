from django.db import models


class BaseModel(models.Model):
    objects = models.Manager

    class Meta:
        abstract = True


class Menu(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menus')
    file = models.FileField(upload_to='menu-files')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
