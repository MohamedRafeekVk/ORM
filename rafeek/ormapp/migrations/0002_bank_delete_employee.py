# Generated by Django 5.1.3 on 2024-11-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accountno', models.IntegerField(primary_key='accountno', serialize=False)),
                ('Aadharno', models.IntegerField()),
                ('DoB', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Branch', models.CharField(max_length=21)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
