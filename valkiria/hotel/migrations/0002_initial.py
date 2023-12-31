# Generated by Django 4.2.5 on 2023-10-26 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hotel", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="habitacionDetalle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="hotel.habitaciondetalle",
            ),
        ),
        migrations.AddField(
            model_name="habitaciondetalle",
            name="habitacion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hotel.habitaciones"
            ),
        ),
        migrations.AddField(
            model_name="factura",
            name="reserva",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hotel.reserva"
            ),
        ),
    ]
