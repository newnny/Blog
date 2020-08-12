#Everytime when you make models or change models, run this
#python manage.py makemigrations
#python manage.py migrate

from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'degault.jpg', blank =True)
    # add in thumbnail urlpatterns
    # add in auther later
    
    def __str__(self):
        return self.title

    def shortbody(self):
        return self.body[:50] + '...'
