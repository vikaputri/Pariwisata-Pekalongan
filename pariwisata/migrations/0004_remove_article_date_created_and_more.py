# Generated by Django 4.0.5 on 2022-06-14 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pariwisata', '0003_article_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date_modified',
        ),
    ]
