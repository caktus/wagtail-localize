# Generated by Django 2.2.12 on 2020-05-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_workflow', '0002_change_foreign_key_on_delete_behaviours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translationrequest',
            name='target_root',
        ),
    ]