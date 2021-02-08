# Generated by Django 3.1.5 on 2021-02-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('wisely', '0008_auto_20210121_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='anchor',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('data', models.TextField()),
            ],
        ),
    ]