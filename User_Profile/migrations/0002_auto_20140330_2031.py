# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='about',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
