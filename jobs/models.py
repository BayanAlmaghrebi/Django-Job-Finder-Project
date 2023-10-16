from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    title = models.CharField(('Title'),max_length=120)
    overview = models.TextField(('Overview'),max_length=500)
    description = models.TextField(('Description'),max_length=100000)
    Job_Type = models.TextField(('Job_Type'),max_length=50)
    Job_Location = models.TextField(('Job_Location'),max_length=500)
    image = models.ImageField(('Image'),upload_to='jobs')
    salary = models.FloatField(('Salary'))
    requirments = models.TextField(('Requirments'),max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey('Company',verbose_name=_('Company'),related_name='job_company',on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Job, self).save(*args, **kwargs)

class company(models.Model):
    title = models.CharField(('Title'),max_length=120)
    image = models.ImageField(('Image'),upload_to='company')
    company_information = models.TextField(('Company_information'),max_length=5000)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(company, self).save(*args, **kwargs)