from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='student/', verbose_name='аватар', **NULLABLE)
    email = models.CharField(max_length=150, verbose_name='email', unique=True, **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Учится?')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name', )
