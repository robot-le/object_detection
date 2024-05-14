from django.db import models


class Image(models.Model):
    image = models.ImageField('Uploaded image')


class DetectedObjects(models.Model):
    label = models.CharField(max_length=255)
    confidence = models.FloatField()
    bounding_box = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
