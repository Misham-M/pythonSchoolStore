# Generated by Django 4.2.6 on 2023-10-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolStore", "0004_alter_details_paper_alter_details_pen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="details",
            name="paper",
            field=models.CharField(default=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="details",
            name="pen",
            field=models.CharField(default=False, max_length=10, null=True),
        ),
    ]
