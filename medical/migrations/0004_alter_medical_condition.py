# Generated by Django 4.2.5 on 2024-06-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medical", "0003_alter_medical_condition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medical",
            name="condition",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=100,
                null=True,
                verbose_name="コンディション",
            ),
        ),
    ]
