# Generated by Django 5.1.3 on 2025-04-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=400)),
                ('Location', models.CharField(max_length=300)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
