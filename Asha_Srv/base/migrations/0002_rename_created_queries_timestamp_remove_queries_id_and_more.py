# Generated by Django 4.0.5 on 2023-12-09 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queries',
            old_name='created',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='queries',
            name='id',
        ),
        migrations.RemoveField(
            model_name='queries',
            name='query',
        ),
        migrations.AddField(
            model_name='queries',
            name='answer_text',
            field=models.TextField(default='A'),
        ),
        migrations.AddField(
            model_name='queries',
            name='imageResponse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='queries',
            name='query_id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='queries',
            name='query_text',
            field=models.TextField(default='Q'),
        ),
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('query_text', models.TextField()),
                ('answer_text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]