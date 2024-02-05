# Generated by Django 5.0.1 on 2024-01-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_details', models.CharField(max_length=45)),
                ('quantity', models.IntegerField()),
                ('vendor_name', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=70)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
