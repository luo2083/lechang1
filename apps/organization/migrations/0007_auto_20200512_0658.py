# Generated by Django 2.0.1 on 2020-05-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_courseorg_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='国内名校', max_length=20, verbose_name='机构标签'),
        ),
    ]
