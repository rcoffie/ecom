# Generated by Django 4.0.5 on 2022-06-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
