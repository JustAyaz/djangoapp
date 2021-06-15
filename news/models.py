from django.db import models


class Links(models.Model):
    link = models.CharField(max_length=100, blank=True)
    my_link = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.link
