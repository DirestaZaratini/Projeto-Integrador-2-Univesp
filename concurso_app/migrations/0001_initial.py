# Generated by Django 5.0.3 on 2024-09-19 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_processo', models.CharField(max_length=50)),
                ('area_concurso', models.CharField(max_length=100)),
                ('orgao_realizador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Examinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examinadores', to='concurso_app.concurso')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='concurso_app.candidato')),
                ('examinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concurso_app.examinador')),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('eliminatoria', models.BooleanField(default=False)),
                ('peso', models.FloatField()),
                ('num_pessoas', models.IntegerField()),
                ('concurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provas', to='concurso_app.concurso')),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='prova',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidatos', to='concurso_app.prova'),
        ),
    ]
