# Generated by Django 3.1.5 on 2021-01-21 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wisely', '0006_auto_20210115_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morning_entry',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
