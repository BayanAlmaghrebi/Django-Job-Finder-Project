# Generated by Django 4.2.6 on 2023-10-16 19:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('image', models.ImageField(upload_to='company', verbose_name='Image')),
                ('company_information', models.TextField(max_length=5000, verbose_name='Company_information')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('overview', models.TextField(max_length=500, verbose_name='Overview')),
                ('description', models.TextField(max_length=100000, verbose_name='Description')),
                ('Job_Type', models.TextField(max_length=50, verbose_name='Job_Type')),
                ('Job_Location', models.TextField(max_length=500, verbose_name='Job_Location')),
                ('image', models.ImageField(upload_to='jobs', verbose_name='Image')),
                ('salary', models.FloatField(verbose_name='Salary')),
                ('requirments', models.TextField(max_length=5000, verbose_name='Requirments')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_company', to='jobs.company', verbose_name='Company')),
            ],
        ),
    ]
