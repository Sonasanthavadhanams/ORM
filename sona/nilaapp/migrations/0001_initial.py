# Generated by Django 5.1.2 on 2024-10-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Accountnumber', models.IntegerField(primary_key='Accountnumber', serialize=False)),
                ('Moblienumber', models.IntegerField()),
                ('Startingdate', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Amount', models.IntegerField()),
                ('Interest', models.FloatField()),
                ('Endingdate', models.IntegerField()),
            ],
        ),
    ]