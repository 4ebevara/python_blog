# Generated by Django 5.1.6 on 2025-03-07 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_publication_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='blog.category'),
        ),
    ]
