# Generated by Django 3.1.6 on 2021-03-20 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanType',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('no_of_courses', models.IntegerField()),
                ('no_of_students_per_course', models.IntegerField()),
                ('prog_assign_enabled', models.BooleanField()),
                ('subjective_lab_enabled', models.BooleanField()),
                ('email_enabled', models.BooleanField()),
                ('per_video_limit', models.FloatField()),
                ('per_video_limit_unit',
                 models.CharField(choices=[('KB', 'Kilobytes'),
                                           ('MB', 'MegaBytes'),
                                           ('GB', 'GigaBytes'),
                                           ('TB', 'TeraBytes')],
                                  max_length=2)),
                ('total_video_limit', models.FloatField()),
                ('total_video_limit_unit',
                 models.CharField(choices=[('KB', 'Kilobytes'),
                                           ('MB', 'MegaBytes'),
                                           ('GB', 'GigaBytes'),
                                           ('TB', 'TeraBytes')],
                                  max_length=2)),
                ('subjective_lab_submission_size_per_student',
                 models.FloatField()),
                ('subjective_lab_submission_size_per_student_unit',
                 models.CharField(choices=[('KB', 'Kilobytes'),
                                           ('MB', 'MegaBytes'),
                                           ('GB', 'GigaBytes'),
                                           ('TB', 'TeraBytes')],
                                  max_length=2)),
                ('plan_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='registration.plantype')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionHistory',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField()),
                ('purchased_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('subscription',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='registration.subscription')),
                ('user',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
