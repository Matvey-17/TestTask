from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name
