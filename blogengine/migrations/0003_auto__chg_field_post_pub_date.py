# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.pub_date'
        db.alter_column(u'blogengine_post', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Post.pub_date'
        db.alter_column(u'blogengine_post', 'pub_date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'blogengine.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blogengine']