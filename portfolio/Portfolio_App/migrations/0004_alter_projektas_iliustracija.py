# Generated by Django 4.2.3 on 2023-07-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_App', '0003_alter_projektas_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektas',
            name='iliustracija',
            field=models.ImageField(blank=True, null=True, upload_to='projektas'),
        ),
    ]