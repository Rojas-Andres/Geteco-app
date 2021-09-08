# Generated by Django 2.2.9 on 2021-09-08 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='getecoapp.Ciudad', verbose_name='ciudad_empleado')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='getecoapp.Empresa', verbose_name='empresa_empleado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
