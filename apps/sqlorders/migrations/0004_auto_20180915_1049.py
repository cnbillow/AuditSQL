# Generated by Django 2.1.1 on 2018-09-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0003_auto_20180914_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqlordersenvironment',
            name='envi_id',
            field=models.IntegerField(default=1, verbose_name='ID，起始值：1'),
        ),
        migrations.AlterField(
            model_name='sqlordersenvironment',
            name='parent_id',
            field=models.IntegerField(default=0, verbose_name='父ID，起始值：0'),
        ),
    ]
