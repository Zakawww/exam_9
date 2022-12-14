# Generated by Django 4.1.1 on 2022-09-24 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_albums_alter_photo_photo_delete_comment_albums_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='note',
            field=models.CharField(max_length=100, verbose_name='Подпись'),
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments', to='webapp.photo', verbose_name='Фото'),
        ),
    ]
