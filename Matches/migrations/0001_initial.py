# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('user2', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('offering', models.CharField(max_length=40, null=True, db_index=True)),
                ('recieving', models.CharField(max_length=40, null=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
