# Generated by Django 4.2.16 on 2024-10-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='tickets/images/', verbose_name='Image'),
        ),
    ]
