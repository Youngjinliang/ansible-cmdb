# Generated by Django 2.0.1 on 2018-07-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_auto_20180726_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='describe_message',
            name='system_kernel',
            field=models.TextField(),
        ),
    ]