# Generated by Django 3.2.9 on 2021-11-28 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True, verbose_name='demo_link')),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True, verbose_name='source_link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='id')),
            ],
        ),
    ]
