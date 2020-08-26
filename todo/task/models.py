from django.db import models

# Create your models here.
class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done') 
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)

    def setDone(self):
        if self.status != self.DONE:
            self.status = self.DONE
            self.save()
            return self.DONE
        return "have done"

    def __str__(self):
        return self.description
