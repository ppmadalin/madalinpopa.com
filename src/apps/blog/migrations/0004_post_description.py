# Generated by Django 3.1.5 on 2021-01-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=160, null=True),
        ),
    ]
