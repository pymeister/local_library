# Generated by Django 3.0.8 on 2020-07-30 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]