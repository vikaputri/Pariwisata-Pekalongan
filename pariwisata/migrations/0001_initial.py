# Generated by Django 4.0.5 on 2022-06-08 04:19

import ckeditor.fields
from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('alamat', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=12)),
                ('jam', models.CharField(max_length=15)),
                ('harga', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='destinasi')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('article', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='pariwisata.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Category',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='category', to='pariwisata.category'),
        ),
    ]
