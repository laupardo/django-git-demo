# Generated by Django 3.1.6 on 2021-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('breed', models.CharField(blank=True, max_length=45, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'dogs',
                'managed': False,
            },
        ),
    ]
