from django.db import models

# Create your models here.
class TaskList(models.Model):
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    # due_date=models.DateField(null=True)

    class Meta:
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')

    def __str__(self):
       return  self.task