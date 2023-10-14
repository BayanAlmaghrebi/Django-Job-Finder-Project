from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(('Title'),max_length=120)
    overview = models.TextField(('Overview'),max_length=500)
    description = models.TextField(('Description'),max_length=100000)
    Job_Type = models.TextField(('Overview'),max_length=50)
    Job_Location = models.TextField(('Overview'),max_length=500)
    image = models.ImageField(('Image'),upload_to='jobs')
    salary = models.FloatField(('Salary'))
    company
