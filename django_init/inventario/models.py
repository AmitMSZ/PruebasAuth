from django.db import models

# Create your models here.


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(
        verbose_name='Nombre de Bodega', max_length=30, unique=True)

    class Meta:
        db_table = 'warehouse'
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'

    def __str__(self):
        return self.warehouse_name


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(
        verbose_name='Nombre de Tipo', max_length=30, unique=True)

    class Meta:
        db_table = 'type'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.type_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(
        verbose_name='Nombre de Producto', max_length=30)
    product_description = models.TextField(
        verbose_name='Descripción de Producto', null=True, blank=True)
    product_stock = models.IntegerField(verbose_name='Stock de Producto')
    type = models.ForeignKey(
        Type, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.product_name
