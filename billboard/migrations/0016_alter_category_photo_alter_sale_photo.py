# Generated by Django 5.0.7 on 2025-04-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0015_alter_category_photo_alter_sale_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='static/media/category-new_MROs2uS.png', upload_to='static/media/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='photo',
            field=models.ImageField(default='static/media/category-new_MROs2uS.png', upload_to='static/media/', verbose_name='Фото'),
        ),
    ]
