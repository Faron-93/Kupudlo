# Generated by Django 3.0.2 on 2020-06-16 20:05

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gielda_ogloszenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=50)),
                ('typ', models.CharField(choices=[('KL', 'KLAPÓWKA'), ('TC', 'TACKA'), ('WR', 'WRAP'), ('AR', 'ARKUSZ'), ('PR', 'PRZEKŁADKA'), ('AT', 'AUTOMATYCZNE')], default='KL', max_length=2)),
                ('opis', models.TextField(default='Brak')),
                ('ilosc', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0)])),
                ('data_dodania', models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 5, 51, 2895, tzinfo=utc))),
                ('lokalizacja', models.CharField(max_length=30)),
                ('cena', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
