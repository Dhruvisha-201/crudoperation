# Generated by Django 4.0.5 on 2022-06-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0004_rename_student_employee_alter_employee_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
    ]
