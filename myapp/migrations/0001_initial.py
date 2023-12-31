# Generated by Django 4.0 on 2023-12-23 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('avatar', models.ImageField(upload_to='media/profile')),
                ('phoneNumber', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='media/products')),
                ('price', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('NA', 'Noactive')], default='NA', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persons')),
            ],
        ),
    ]
