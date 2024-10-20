# Generated by Django 4.2.16 on 2024-10-18 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Tag Name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('urgent', 'Urgent')], default='medium', max_length=10, verbose_name='Priority')),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed'), ('on_hold', 'On Hold')], default='open', max_length=30, verbose_name='Status')),
                ('closed_at', models.DateTimeField(blank=True, null=True, verbose_name='Closed At')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets_assigned', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='ticket.category')),
                ('tags', models.ManyToManyField(blank=True, to='ticket.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['create_at'],
            },
        ),
    ]
