# Generated by Django 3.1.5 on 2021-01-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('title', models.CharField(max_length=50)),
                ('descriptsion', models.TextField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리 목록',
                'ordering': ('title',),
            },
        ),
    ]