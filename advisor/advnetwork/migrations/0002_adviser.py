# Generated by Django 3.1.7 on 2021-05-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advnetwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adname', models.CharField(max_length=100)),
                ('ad_id', models.IntegerField(max_length=100)),
                ('bookingtime', models.IntegerField(max_length=100)),
                ('bookid', models.IntegerField()),
            ],
        ),
    ]