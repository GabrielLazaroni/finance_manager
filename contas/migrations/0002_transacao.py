# Generated by Django 4.1 on 2022-08-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descriçao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
