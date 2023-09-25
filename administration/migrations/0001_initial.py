# Generated by Django 4.2.4 on 2023-09-15 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(choices=[('darkred', 'Dunkelrot'), ('red', 'Rot'), ('darkorange', 'Dunkelorange'), ('orange', 'Orange'), ('lightgreen', 'Hellgrün'), ('darkgreen', 'Dunkelgrün'), ('darkcyan', 'Türkis'), ('lightblue', 'Hellblau'), ('darkblue', 'Dunkelblau'), ('mediumpurple', 'Violett'), ('hotpink', 'Rosa'), ('gray', 'Grau'), ('brown', 'Braun'), ('black', 'Schwarz')], default='black', max_length=20)),
                ('permissions', models.ManyToManyField(blank=True, related_name='roles', to='administration.custompermission')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('READ', 'Lesen'), ('CREATE', 'Erstellen'), ('EDIT', 'Bearbeiten'), ('DELETE', 'Löschen')], max_length=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('model_name', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]