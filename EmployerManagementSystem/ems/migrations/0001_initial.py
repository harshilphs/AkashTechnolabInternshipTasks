# Generated by Django 3.1.7 on 2021-05-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAdmin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_email', models.EmailField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
            ],
        ),
    ]
