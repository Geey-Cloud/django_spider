# Generated by Django 4.0.4 on 2022-04-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('mid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=5, null=True)),
                ('face', models.CharField(blank=True, max_length=1000, null=True)),
                ('level', models.CharField(blank=True, max_length=10, null=True)),
                ('follower', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
