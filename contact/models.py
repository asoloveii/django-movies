from django.db import models


class Contact(models.Model):

    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.email
