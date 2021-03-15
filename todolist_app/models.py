from django.db import models







class Tasklist(models.Model):
    Taskname=models.CharField(max_length=300)
    task_status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Taskname



