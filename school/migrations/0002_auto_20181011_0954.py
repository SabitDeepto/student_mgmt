# Generated by Django 2.1.1 on 2018-10-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='Stablished_date',
            field=models.DateField(),
        ),
    ]