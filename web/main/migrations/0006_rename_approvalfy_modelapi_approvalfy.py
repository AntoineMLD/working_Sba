# Generated by Django 4.2.11 on 2024-03-05 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_modelapi_approvaldate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelapi',
            old_name='ApprovalFY',
            new_name='ApprovalFy',
        ),
    ]
