# Generated by Django 3.1.6 on 2021-03-29 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjective_assignments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectiveassignmenthistory',
            name='submitted_by',
        ),
    ]