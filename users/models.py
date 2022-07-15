from django.db import models

class User(models.Model):
    use_in_migrations = True
    email = models.CharField(primary_key=True, max_length=128)
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    birth = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.email}'