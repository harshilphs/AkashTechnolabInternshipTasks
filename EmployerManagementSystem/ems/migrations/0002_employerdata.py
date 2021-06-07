# Generated by Django 3.1.7 on 2021-05-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.EmailField(max_length=15)),
                ('design', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
            ],
        ),
    ]