# Generated by Django 3.1.6 on 2021-03-19 14:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programming_assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedprogrammingassignment',
            name='files_to_be_submitted',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                null=True,
                size=None),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assignmentsection',
            name='compiler_command',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsection',
            name='execution_command',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsection',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='simpleprogrammingassignment',
            name='programming_language',
            field=models.CharField(choices=[('C', 'C'), ('C++', 'C++'),
                                            ('Java', 'Java'),
                                            ('Python', 'Python'),
                                            ('Others', 'Others')],
                                   default='C',
                                   max_length=10),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='cmd_line_args',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                null=True,
                size=None),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
