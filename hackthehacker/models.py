from django.db import models

class HackerInfo(models.Model):
    ip = models.CharField(max_length=255)

    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        blank=True,
        null=True
    )

    country_iso = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    subdivisions = models.CharField(max_length=255, null=True, blank=True)
    subdivisions_iso = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal = models.CharField(max_length=255, null=True, blank=True)
    lng = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)