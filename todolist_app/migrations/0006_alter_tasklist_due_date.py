# Generated by Django 3.2.7 on 2021-09-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_alter_tasklist_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
