# Generated by Django 3.1.5 on 2021-04-22 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Seller_Mobile', models.CharField(max_length=15)),
                ('Price_Range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.position')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
