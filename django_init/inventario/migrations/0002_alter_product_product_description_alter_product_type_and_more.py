# Generated by Django 4.1.2 on 2022-11-25 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Descripción de Producto"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="inventario.type"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="warehouse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="inventario.warehouse"
            ),
        ),
        migrations.AlterField(
            model_name="type",
            name="type_name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Nombre de Tipo"
            ),
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="warehouse_name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Nombre de Bodega"
            ),
        ),
    ]
