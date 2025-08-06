from django.db import models


# нужна моделька для авторов
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title