# Generated by Django 4.1.1 on 2022-09-24 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_photo_description_remove_photo_name_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='webapp.album', verbose_name='Альбом'),
        ),
    ]
