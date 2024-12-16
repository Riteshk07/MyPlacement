# Generated by Django 4.1 on 2023-01-02 13:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied', models.BooleanField(default=False)),
                ('reffred', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('selected', models.BooleanField(default=False)),
                ('apply_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement.new_job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Saved_Job',
                'ordering': ('id',),
            },
        ),
    ]