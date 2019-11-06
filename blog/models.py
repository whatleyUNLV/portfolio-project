from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:45]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %-d, %Y')

# Add to the admin
