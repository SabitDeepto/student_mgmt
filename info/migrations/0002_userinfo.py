# Generated by Django 2.1.1 on 2018-10-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default=1, max_length=100)),
                ('Population', models.CharField(max_length=100)),
            ],
        ),
    ]