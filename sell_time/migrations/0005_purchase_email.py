# Generated by Django 5.2 on 2025-05-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_time', '0004_alter_purchase_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
