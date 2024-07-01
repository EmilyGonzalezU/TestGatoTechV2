# Generated by Django 5.0.6 on 2024-06-16 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('descuento', models.CharField(blank=True, max_length=60, null=True)),
                ('precio_anterior', models.CharField(blank=True, max_length=60, null=True)),
                ('precio_transferencia', models.CharField(max_length=60, null=True)),
                ('precio_normal', models.CharField(max_length=60, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='gt_store/')),
                ('categoria', models.CharField(choices=[('pc', 'PC'), ('notebook', 'Notebook'), ('mouse', 'Mouse'), ('teclado', 'Teclado'), ('audifonos', 'Audifonos'), ('procesador', 'Procesador'), ('ram', 'Memoria RAM'), ('placa_madre', 'Placa Madre'), ('tarjeta_video', 'Tarjeta de Video'), ('fuente_poder', 'Fuente de Poder'), ('almacenamiento', 'Almacenamiento'), ('gabinete', 'Gabinete'), ('monitor', 'Monitor')], default='pc', max_length=20)),
                ('procesador', models.CharField(blank=True, max_length=60, null=True)),
                ('memoria_ram', models.CharField(blank=True, max_length=60, null=True)),
                ('almacenamiento', models.CharField(blank=True, max_length=60, null=True)),
                ('tarjeta_video', models.CharField(blank=True, max_length=60, null=True)),
                ('fuente_poder', models.CharField(blank=True, max_length=60, null=True)),
                ('placa_madre', models.CharField(blank=True, max_length=60, null=True)),
                ('refrigeracion', models.CharField(blank=True, max_length=60, null=True)),
                ('gabinete', models.CharField(blank=True, max_length=60, null=True)),
                ('tamano_pantalla', models.CharField(blank=True, max_length=60, null=True)),
                ('resolucion_pantalla', models.CharField(blank=True, max_length=60, null=True)),
                ('bateria', models.CharField(blank=True, max_length=60, null=True)),
                ('dpi', models.IntegerField(blank=True, null=True)),
                ('tracking', models.CharField(blank=True, max_length=60, null=True)),
                ('sensor', models.CharField(blank=True, max_length=60, null=True)),
                ('tipo_conexion', models.CharField(blank=True, max_length=60, null=True)),
                ('boton', models.BooleanField(default=False)),
                ('numero_botones', models.IntegerField(blank=True, null=True)),
                ('retroiluminacion', models.BooleanField(default=False)),
                ('tipo_teclado', models.CharField(blank=True, max_length=60, null=True)),
                ('distribucion', models.CharField(blank=True, max_length=60, null=True)),
                ('microfono', models.BooleanField(default=False)),
                ('tipo_auricular', models.CharField(blank=True, max_length=60, null=True)),
                ('cancelacion_ruido', models.BooleanField(default=False)),
                ('nucleos', models.IntegerField(blank=True, null=True)),
                ('hilos', models.IntegerField(blank=True, null=True)),
                ('socket', models.CharField(blank=True, max_length=60, null=True)),
                ('capacidad', models.CharField(blank=True, max_length=60, null=True)),
                ('tipo_ram', models.CharField(blank=True, max_length=60, null=True)),
                ('velocidad', models.IntegerField(blank=True, null=True)),
                ('latencia', models.CharField(blank=True, max_length=60, null=True)),
                ('formato', models.CharField(blank=True, max_length=60, null=True)),
                ('chipset', models.CharField(blank=True, max_length=60, null=True)),
                ('soporte_ram', models.CharField(blank=True, max_length=60, null=True)),
                ('memoria', models.CharField(blank=True, max_length=60, null=True)),
                ('tipo_memoria', models.CharField(blank=True, max_length=60, null=True)),
                ('velocidad_reloj', models.CharField(blank=True, max_length=60, null=True)),
                ('interfaz', models.CharField(blank=True, max_length=60, null=True)),
                ('potencia', models.CharField(blank=True, max_length=60, null=True)),
                ('certificacion', models.CharField(blank=True, max_length=60, null=True)),
                ('modularidad', models.CharField(blank=True, max_length=60, null=True)),
                ('tipo_almacenamiento', models.CharField(blank=True, max_length=60, null=True)),
                ('velocidad_lectura', models.IntegerField(blank=True, null=True)),
                ('velocidad_escritura', models.IntegerField(blank=True, null=True)),
                ('numero_bahias', models.IntegerField(blank=True, null=True)),
                ('ventilacion', models.BooleanField(default=False)),
                ('nro_ventiladores', models.IntegerField(blank=True, null=True)),
                ('frecuencia', models.IntegerField(blank=True, null=True)),
                ('tipo_panel', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]