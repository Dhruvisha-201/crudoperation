# Generated by Django 4.0.5 on 2022-06-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_alter_student_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='employee',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
    ]
