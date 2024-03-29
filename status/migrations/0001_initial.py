# Generated by Django 5.0.1 on 2024-02-01 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(blank=True, max_length=30, null=True)),
                ('child_name', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.child')),
                ('upper_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.status')),
            ],
        ),
    ]
