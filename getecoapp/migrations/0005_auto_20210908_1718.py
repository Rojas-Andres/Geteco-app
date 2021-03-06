# Generated by Django 2.2.9 on 2021-09-08 22:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getecoapp', '0004_auto_20210908_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='ciudad',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='getecoapp.Ciudad', verbose_name='ciudad_empleado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getecoapp.Empresa', verbose_name='empresa_empleado'),
        ),
    ]
