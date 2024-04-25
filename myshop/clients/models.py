from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):


    class Meta:
        db_table = 'client'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

