# Generated by Django 4.2.3 on 2023-07-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='lname',
            field=models.CharField(max_length=100),
        ),
    ]