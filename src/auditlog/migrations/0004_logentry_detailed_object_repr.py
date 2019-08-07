# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0003_logentry_detailed_object_repr'),
        ('auditlog', '0003_logentry_remote_addr'),
   ]

    operations = [
            # In Prism fork we added detailed_object_repr field
            # For same purpose main repo added additional_data field
            # So, here instead of adding additional_data we rename 
            # our detailed_object_repr to additional_data

            #migrations.AddField(
            #  model_name='logentry',
            #  name='additional_data',
            #  field=jsonfield.fields.JSONField(null=True, blank=True),
            migrations.RenameField(
                        model_name='logentry',
                        old_name='oldname',
                        new_name='newname',
                       ),
        ),
    ]
