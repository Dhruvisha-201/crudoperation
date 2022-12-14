# Generated by Django 4.0.5 on 2022-06-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='uniq',
            fields=[
                ('uniq_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('hobbies', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
