# Generated by Django 5.2 on 2025-05-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration_minutes', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('use_type', models.CharField(choices=[('future', 'Towards Your Future'), ('past', 'For Your Past')], default='future', max_length=10)),
            ],
        ),
    ]
