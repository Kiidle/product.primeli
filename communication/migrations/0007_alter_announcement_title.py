# Generated by Django 3.2.20 on 2023-11-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0006_alter_announcement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
    ]