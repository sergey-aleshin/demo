# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Host.modified'
        db.add_column(u'ipmanager_host', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Host.modified'
        db.delete_column(u'ipmanager_host', 'modified')


    models = {
        u'ipmanager.host': {
            'Meta': {'object_name': 'Host'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ipmanager']