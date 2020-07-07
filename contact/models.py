#Everytime when you make models or change models, run this
#python manage.py makemigrations
#python manage.py migrate

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    subject = models.CharField(max_length = 150)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # add in thumbnail urlpatterns
    # add in auther later


    def __str__(self):
        return self.name
