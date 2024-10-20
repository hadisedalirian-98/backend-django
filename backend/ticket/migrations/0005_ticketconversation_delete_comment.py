# Generated by Django 4.2.16 on 2024-10-20 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0004_profile_remove_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=30, verbose_name='Status')),
                ('started_at', models.DateField(auto_now_add=True, verbose_name='Started At')),
                ('ended_at', models.DateTimeField(blank=True, null=True, verbose_name='Ended At')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handled_conversations', to=settings.AUTH_USER_MODEL)),
                ('tickets', models.ManyToManyField(related_name='conversations', to='ticket.ticket')),
            ],
            options={
                'verbose_name': 'TicketConversation',
                'verbose_name_plural': 'TicketConversations',
                'ordering': ['subject'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
