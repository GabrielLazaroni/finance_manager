# Generated by Django 4.1 on 2022-08-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0006_alter_transacao_options_alter_transacao_observacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
