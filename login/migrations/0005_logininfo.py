# Generated by Django 4.0.4 on 2022-04-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
