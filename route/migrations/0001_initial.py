# Generated by Django 2.2 on 2019-09-12 13:18

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=100, unique=True)),
                ('creation_date', models.DateField()),
                ('length', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('last_point', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='last_point_on_route', to='route.Point')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='route.Route'),
        ),
    ]
