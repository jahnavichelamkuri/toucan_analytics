# Generated by Django 4.2.1 on 2023-05-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMIData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_Id', models.IntegerField()),
                ('EMI_paid_on_time', models.CharField(max_length=6)),
            ],
        ),
    ]