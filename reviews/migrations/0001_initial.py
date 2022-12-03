# Generated by Django 4.1.2 on 2022-11-04 17:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stars', models.PositiveIntegerField()),
                ('rating', models.CharField(max_length=600)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='books.book')),
            ],
        ),
    ]
