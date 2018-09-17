# Generated by Django 2.0.1 on 2018-09-17 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dano',
            fields=[
                ('idDano', models.AutoField(primary_key=True, serialize=False)),
                ('dataDano', models.DateField()),
                ('descricao', models.TextField()),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendendias', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('patrimonio', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('statusRecurso', models.CharField(default='Disponivel', max_length=45)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoriaRecurso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('statusReserva', models.CharField(default='Reservado', max_length=45)),
                ('dataReserva', models.DateField()),
                ('horaReserva', models.TimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('dataEmprestimo', models.DateField(null=True)),
                ('horaEmprestimo', models.TimeField(null=True)),
                ('dataDevolucao', models.DateField(null=True)),
                ('horaDevolucao', models.TimeField(null=True)),
                ('dataDevolucaoEfetiva', models.DateField(blank=True, null=True)),
                ('horaDevolucaoEfetiva', models.TimeField(blank=True, null=True)),
                ('recursos', models.ManyToManyField(blank=True, db_table='ReservaRecurso', related_name='reserva', to='recursos.Recurso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dano',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos.Reserva'),
        ),
    ]