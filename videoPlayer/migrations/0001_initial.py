# Generated by Django 4.0.1 on 2022-01-06 00:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlEntry',
            fields=[
                ('id_url', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('add_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
