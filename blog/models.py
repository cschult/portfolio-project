from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        # return self.pub_date.date()
        return self.pub_date.strftime("%Y-%m-%d %H:%M:%S")
        # return self.pub_date.strftime("%c")
