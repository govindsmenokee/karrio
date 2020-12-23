# Generated by Django 3.1.4 on 2020-12-22 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import purpleserver.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0003_auto_20201222_1042'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=purpleserver.core.models.uuid, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.address')),
                ('customs', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.customs')),
                ('parcel', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.parcel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'template',
                'ordering': ['-created_at'],
            },
        ),
    ]
