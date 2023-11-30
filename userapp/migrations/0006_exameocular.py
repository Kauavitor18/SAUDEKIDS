# Generated by Django 4.2.7 on 2023-11-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_remove_vacina_datavacina'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExameOcular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('globo_ocular', models.CharField(choices=[('normal', 'Normal'), ('anormal', 'Anormal')], default='normal', max_length=10)),
                ('pupilas', models.CharField(choices=[('normal', 'Normal'), ('anormal', 'Anormal')], default='normal', max_length=10)),
                ('estrabismo', models.CharField(choices=[('nao', 'Não'), ('sim', 'Sim')], default='nao', max_length=5)),
                ('secrecao_ocular', models.CharField(choices=[('nao', 'Não'), ('sim', 'Sim')], default='nao', max_length=5)),
            ],
        ),
    ]
