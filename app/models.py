from django.db import models

class Medicine(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, unique=True, blank=False, max_length=150)
    price = models.PositiveSmallIntegerField(null=False, blank=False)
    units = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        db_table = "medicine"

    def __str__(self):
        return self.name
