from datetime import datetime

from django.db import models

class News(models.Model):
    post = models.CharField("Title", max_length=255)
    desc = models.TextField("Description")
    image = models.CharField("Reference", max_length=500)
    date = models.DateTimeField("Date", default=datetime.now)

    def __str__(self):
        return self.post
