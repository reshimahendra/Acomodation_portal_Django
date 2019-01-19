# Generated by Django 2.1.1 on 2018-10-01 08:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_type', models.PositiveSmallIntegerField(choices=[(0, 'Visitor review Listing'), (1, 'Provider review Visitor')])),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('content', models.CharField(max_length=4095)),
                ('submitted_on', models.DateField(default=datetime.date.today)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertising.Listing')),
            ],
        ),
    ]