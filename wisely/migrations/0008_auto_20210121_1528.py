# Generated by Django 3.1.5 on 2021-01-21 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wisely', '0007_auto_20210121_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evening_entry',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
