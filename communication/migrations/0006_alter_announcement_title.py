# Generated by Django 3.2.20 on 2023-11-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0005_alter_announcement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
