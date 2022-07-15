from datetime import datetime

from books.models import Book
from users.models import User
from django.db import models

class Comment(models.Model):
    use_in_migrations = True
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    auto_recode = models.TextField()
    reg_date = models.DateField(default=datetime.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f'{self.pk} {self.comment_id}'
