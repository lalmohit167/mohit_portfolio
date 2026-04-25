from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    tech_stack = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title

    def tech_list(self):
        return self.tech_stack.split(',')