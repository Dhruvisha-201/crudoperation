# Generated by Django 4.0.5 on 2022-06-22 13:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0007_uniq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniq',
            name='hobbies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('reading', 'reading'), ('writing', 'writing'), ('music', 'music')], max_length=21),
        ),
    ]
