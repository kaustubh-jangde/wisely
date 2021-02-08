# Generated by Django 3.1.5 on 2021-01-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisely', '0004_auto_20210114_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evening_entry',
            name='data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='evening_entry',
            name='date_id',
            field=models.DateField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='evening_entry',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='morning_entry',
            name='data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='morning_entry',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='morning_entry',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
