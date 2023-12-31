# Generated by Django 4.2.6 on 2023-10-29 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateTimeField(blank=True, null=True)),
                ('correo', models.CharField(max_length=60)),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='habitaciondetalle',
            name='habitacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.habitaciones'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.usuario'),
        ),
    ]
