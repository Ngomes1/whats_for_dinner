# Generated by Django 4.0.3 on 2022-04-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.TextField(default='No Comment', max_length=12000),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(default='Add Ingredients & Amount Here', max_length=12000),
        ),
        migrations.AddField(
            model_name='recipes',
            name='instructions',
            field=models.TextField(default='Instruction/Meal Preps Go Here', max_length=12000),
        ),
    ]