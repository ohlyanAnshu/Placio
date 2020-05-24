# Generated by Django 3.0.5 on 2020-05-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placiosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='indexForm',
        ),
    ]