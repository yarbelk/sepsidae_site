# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contributor.user'
        db.delete_column(u'contribs_contributor', 'user_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Contributor.user'
        raise RuntimeError("Cannot reverse this migration. 'Contributor.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contributor.user'
        db.add_column(u'contribs_contributor', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True),
                      keep_default=False)


    models = {
        u'contribs.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'staff'", 'to': u"orm['contribs.Institution']"})
        },
        u'contribs.institution': {
            'Meta': {'object_name': 'Institution'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contribs']