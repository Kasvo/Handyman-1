# Generated by Django 3.0.8 on 2020-07-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessuser', '0003_auto_20200728_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional_user',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
    ]
