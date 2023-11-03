# Generated by Django 4.1.7 on 2023-04-16 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("providers", "0050_carrier_is_system_alter_carrier_metadata_and_more"),
        ("orgs", "0012_auto_20221130_0304"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarrierConfigLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="providers.carrierconfig",
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrier_config_links",
                        to="orgs.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organization",
            name="carrier_configs",
            field=models.ManyToManyField(
                related_name="org",
                through="orgs.CarrierConfigLink",
                to="providers.carrierconfig",
            ),
        ),
    ]