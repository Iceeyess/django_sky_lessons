from django.db import models
from materials.apps import MaterialsConfig
# Create your models here.

app_name = MaterialsConfig.name
nulls = dict(blank=True, null=True)

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='содержимое')
    views_count = models.IntegerField(default=0, verbose_name=' просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', **nulls)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'