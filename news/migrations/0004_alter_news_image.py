# Generated by Django 4.2.3 on 2023-12-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, upload_to="img"),
        ),
    ]
