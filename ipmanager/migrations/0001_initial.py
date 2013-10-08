# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table(u'ipmanager_host', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'ipmanager', ['Host'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table(u'ipmanager_host')


    models = {
        u'ipmanager.host': {
            'Meta': {'object_name': 'Host'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['ipmanager']