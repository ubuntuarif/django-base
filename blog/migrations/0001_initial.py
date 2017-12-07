# Generated by Django 2.0 on 2017-12-05 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Deleted Time', null=True, verbose_name='DateTime Updated')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique Identifier.', unique=True, verbose_name='Unique Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Keep this record active or not.', verbose_name='Active')),
                ('is_archived', models.BooleanField(default=False, help_text='Keep this record active or not.', verbose_name='Is Archived')),
                ('name', models.CharField(blank=True, help_text='User ID document number.', max_length=128, null=True, verbose_name='Document Number')),
                ('created_by', models.ForeignKey(blank=True, help_text='User Who Create This Record', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, help_text='User Who Last Update This Record', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'blog_categories',
            },
        ),
    ]