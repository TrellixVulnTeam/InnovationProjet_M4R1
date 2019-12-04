# Generated by Django 2.2.7 on 2019-12-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0018_auto_20191203_1813'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AlterField(
            model_name='comment',
            name='state_comment',
            field=models.CharField(blank=True, choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6, null=True),
        ),
    ]
