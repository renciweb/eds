# Generated by Django 2.0.7 on 2018-07-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_project_publications'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='projects',
            field=models.ManyToManyField(blank=True, to='content.Project'),
        ),
    ]
