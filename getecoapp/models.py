from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=200)
    class Meta:
        verbose_name = _("Ciudad")
        verbose_name_plural = _("Ciudades")
    def __str__(self):
        return self.nombre_ciudad

class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre_empresa
    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

class Empleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, verbose_name=_("empresa_empleado"), on_delete=models.CASCADE, blank=False, null=False)
    ciudad = models.ForeignKey(Ciudad, verbose_name=_("ciudad_empleado"), on_delete=models.CASCADE, blank=False, null=False)
    fecha_hora_atencion = models.DateField(auto_now=False, auto_now_add=False)
    hora_final_atencion = models.DateField(auto_now=False, auto_now_add=False)
    respuesta = models.TextField()
    fecha_solicitud = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Empleado")
        verbose_name_plural = _("Empleados")
    def __str__(self):
        return self.id