# Generated by Django 3.2.20 on 2023-11-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_auto_20231104_0538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(max_length=3000, verbose_name='Content'),
        ),
    ]
