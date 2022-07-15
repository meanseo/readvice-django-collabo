from django.db import models

class User(models.Model):
    use_in_migrations = True
    email = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=10)
    username = models.CharField()
    birth = models.CharField()
    gender = models.CharField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.email}'