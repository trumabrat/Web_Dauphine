from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return f"{self.text} - {self.author}"
