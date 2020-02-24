from django.db import models
class Contactinfo(models.Model):
    message = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.ImageField(upload_to="profile",default="",blank=True)
    class Meta:
        db_table="contact"
class Signupinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True,null=True, blank=True)
    class Meta:
        db_table="signup"