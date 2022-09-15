from django.db import models

class Users(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
       indexes = [
            models.Index(fields=['first_name',]),
]