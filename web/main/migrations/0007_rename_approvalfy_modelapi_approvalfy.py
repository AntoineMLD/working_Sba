# Generated by Django 4.2.11 on 2024-03-05 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_approvalfy_modelapi_approvalfy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelapi',
            old_name='ApprovalFy',
            new_name='ApprovalFY',
        ),
    ]
