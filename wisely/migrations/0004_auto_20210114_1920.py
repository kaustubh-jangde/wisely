# Generated by Django 3.1.5 on 2021-01-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisely', '0003_evening_entry_morning_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evening_entry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='evening_entry',
            name='key',
        ),
        migrations.RemoveField(
            model_name='evening_entry',
            name='value',
        ),
        migrations.RemoveField(
            model_name='morning_entry',
            name='date_id',
        ),
        migrations.RemoveField(
            model_name='morning_entry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='morning_entry',
            name='key',
        ),
        migrations.RemoveField(
            model_name='morning_entry',
            name='value',
        ),
        migrations.AddField(
            model_name='evening_entry',
            name='data',
            field=models.TextField(default='old'),
        ),
        migrations.AddField(
            model_name='evening_entry',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='morning_entry',
            name='data',
            field=models.TextField(default='old'),
        ),
        migrations.AddField(
            model_name='morning_entry',
            name='date',
            field=models.DateField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='morning_entry',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='evening_entry',
            name='date_id',
            field=models.DateField(default=None, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='container',
        ),
    ]
