# Generated by Django 4.2 on 2023-05-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='arquivo_final',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]