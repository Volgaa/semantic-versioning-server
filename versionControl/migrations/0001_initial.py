# Generated by Django 2.0.3 on 2018-03-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('major_version', models.IntegerField(max_length=3)),
                ('minor_version', models.IntegerField(max_length=3)),
                ('hotfix_version', models.IntegerField(max_length=3)),
                ('build_version', models.IntegerField(max_length=3)),
            ],
        ),
    ]
