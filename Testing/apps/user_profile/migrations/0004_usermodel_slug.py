# Generated by Django 2.2.4 on 2019-08-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20190823_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
    ]
