# Generated by Django 4.2.1 on 2023-08-13 15:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=100)),
                ('members_count', models.PositiveIntegerField()),
                ('users', models.ManyToManyField(related_name='families', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]