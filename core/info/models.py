from django.db import models


class MusicianModel(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'musician'
        verbose_name = 'Musician'
        verbose_name_plural = 'Musicians'
        ordering = ['-name']

    def __str__(self):
        return self.name
