# Generated by Django 4.2.4 on 2023-12-26 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_alter_adress_options_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime', models.CharField(blank=True, max_length=50, null=True)),
                ('judgements', models.TextField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField()),
                ('responsible', models.CharField(blank=True, max_length=50, null=True)),
                ('institution', models.CharField(blank=True, max_length=50, null=True)),
                ('nice2know', models.TextField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criminals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]