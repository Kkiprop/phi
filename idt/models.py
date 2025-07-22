from django.db import models

class Data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class Otpp(models.Model):
    otp = models.CharField(max_length=100)

    def __str__(self):
        return self.otp