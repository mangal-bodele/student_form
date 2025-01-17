# Generated by Django 5.0.3 on 2024-03-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=10)),
                ('ln', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('institute', models.CharField(max_length=50)),
                ('blood_group', models.CharField(choices=[('+ve O', 'O positive'), ('-ve O', 'O negative'), ('+ve A', 'A positive'), ('-ve A', 'A negative'), ('+ve B', 'B positive'), ('-ve B', 'B negative'), ('+ve AB', 'AB positive'), ('-ve AB', 'AB negative')], max_length=10)),
                ('gender', models.CharField(choices=[('male', 'M'), ('Female', 'F'), ('Others', 'O')], max_length=10)),
            ],
        ),
    ]
