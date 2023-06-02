from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zip = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
