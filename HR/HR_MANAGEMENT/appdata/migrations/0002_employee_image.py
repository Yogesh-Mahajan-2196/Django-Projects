# Generated by Django 4.1.4 on 2022-12-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=0, upload_to='emp_image'),
            preserve_default=False,
        ),
    ]
