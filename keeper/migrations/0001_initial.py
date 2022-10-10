# Generated by Django 4.1.2 on 2022-10-10 02:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0002_animal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalKeeper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('origin_country', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/animal_keeper/')),
                ('birth_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_keeper', to='animal.animal')),
            ],
        ),
    ]
