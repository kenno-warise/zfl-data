# Generated by Django 2.2.5 on 2020-07-27 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_godate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogDate',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
