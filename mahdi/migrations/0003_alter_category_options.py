# Generated by Django 4.1.3 on 2022-11-09 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mahdi', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
