from django.db import models
from uuid import uuid4

class Url(models.Model):
    id_url = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.CharField(max_length=100)
    add_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.annotation