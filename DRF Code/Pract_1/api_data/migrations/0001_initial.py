# Generated by Django 4.0.4 on 2022-05-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=20)),
                ('eadd', models.CharField(max_length=200)),
                ('esal', models.FloatField()),
            ],
        ),
    ]
