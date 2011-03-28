# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Area'
        db.create_table('pagina_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
        ))
        db.send_create_signal('pagina', ['Area'])

        # Adding model 'UserProfile'
        db.create_table('pagina_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('extension', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=3)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Area'])),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('casa', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('avatar', self.gf('pagina.thumbs.ImageWithThumbsField')(max_length=100)),
        ))
        db.send_create_signal('pagina', ['UserProfile'])

        # Adding model 'Categoria'
        db.create_table('pagina_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=25, db_index=True)),
        ))
        db.send_create_signal('pagina', ['Categoria'])

        # Adding model 'Seccion'
        db.create_table('pagina_seccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('pagina', ['Seccion'])

        # Adding model 'Subseccion'
        db.create_table('pagina_subseccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Seccion'])),
        ))
        db.send_create_signal('pagina', ['Subseccion'])

        # Adding model 'Link'
        db.create_table('pagina_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('direccion', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('peso', self.gf('django.db.models.fields.IntegerField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Categoria'])),
        ))
        db.send_create_signal('pagina', ['Link'])

        # Adding model 'Archivo'
        db.create_table('pagina_archivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('adjunto1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('subseccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Subseccion'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.UserProfile'])),
        ))
        db.send_create_signal('pagina', ['Archivo'])

        # Adding model 'DiasFeriados'
        db.create_table('pagina_diasferiados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('pagina', ['DiasFeriados'])

        # Adding model 'Noticia'
        db.create_table('pagina_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('texto', self.gf('django.db.models.fields.TextField')(default=' ')),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.UserProfile'])),
        ))
        db.send_create_signal('pagina', ['Noticia'])

        # Adding model 'Actividad'
        db.create_table('pagina_actividad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha1', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='')),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Area'])),
        ))
        db.send_create_signal('pagina', ['Actividad'])

        # Adding M2M table for field participantes on 'Actividad'
        db.create_table('pagina_actividad_participantes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividad', models.ForeignKey(orm['pagina.actividad'], null=False)),
            ('userprofile', models.ForeignKey(orm['pagina.userprofile'], null=False))
        ))
        db.create_unique('pagina_actividad_participantes', ['actividad_id', 'userprofile_id'])

        # Adding model 'Organizacion'
        db.create_table('pagina_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('pagina', ['Organizacion'])

        # Adding model 'TipoContacto'
        db.create_table('pagina_tipocontacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('pagina', ['TipoContacto'])

        # Adding model 'Pais'
        db.create_table('pagina_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=25, db_index=True)),
        ))
        db.send_create_signal('pagina', ['Pais'])

        # Adding model 'Contacto'
        db.create_table('pagina_contacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profesion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Organizacion'])),
            ('email1', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('tel1', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tel2', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('tel3', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('cel1', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('cel2', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('dir1', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('dir2', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.Pais'], null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagina.TipoContacto'], null=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sitio', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('pagina', ['Contacto'])


    def backwards(self, orm):
        
        # Deleting model 'Area'
        db.delete_table('pagina_area')

        # Deleting model 'UserProfile'
        db.delete_table('pagina_userprofile')

        # Deleting model 'Categoria'
        db.delete_table('pagina_categoria')

        # Deleting model 'Seccion'
        db.delete_table('pagina_seccion')

        # Deleting model 'Subseccion'
        db.delete_table('pagina_subseccion')

        # Deleting model 'Link'
        db.delete_table('pagina_link')

        # Deleting model 'Archivo'
        db.delete_table('pagina_archivo')

        # Deleting model 'DiasFeriados'
        db.delete_table('pagina_diasferiados')

        # Deleting model 'Noticia'
        db.delete_table('pagina_noticia')

        # Deleting model 'Actividad'
        db.delete_table('pagina_actividad')

        # Removing M2M table for field participantes on 'Actividad'
        db.delete_table('pagina_actividad_participantes')

        # Deleting model 'Organizacion'
        db.delete_table('pagina_organizacion')

        # Deleting model 'TipoContacto'
        db.delete_table('pagina_tipocontacto')

        # Deleting model 'Pais'
        db.delete_table('pagina_pais')

        # Deleting model 'Contacto'
        db.delete_table('pagina_contacto')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pagina.actividad': {
            'Meta': {'ordering': "('-fecha', 'titulo')", 'object_name': 'Actividad'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Area']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha1': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'participantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pagina.UserProfile']", 'symmetrical': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'pagina.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'adjunto1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subseccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Subseccion']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.UserProfile']"})
        },
        'pagina.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        'pagina.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'pagina.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'cel1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'cel2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dir1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dir2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Organizacion']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Pais']", 'null': 'True', 'blank': 'True'}),
            'profesion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sitio': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tel1': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tel2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'tel3': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.TipoContacto']", 'null': 'True', 'blank': 'True'})
        },
        'pagina.diasferiados': {
            'Meta': {'object_name': 'DiasFeriados'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pagina.link': {
            'Meta': {'ordering': "['peso']", 'object_name': 'Link'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Categoria']"}),
            'direccion': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'peso': ('django.db.models.fields.IntegerField', [], {})
        },
        'pagina.noticia': {
            'Meta': {'ordering': "('-fecha', '-id')", 'object_name': 'Noticia'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.UserProfile']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pagina.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'pagina.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'pagina.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'pagina.subseccion': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Subseccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Seccion']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'pagina.tipocontacto': {
            'Meta': {'object_name': 'TipoContacto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pagina.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagina.Area']"}),
            'avatar': ('pagina.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'extension': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '3'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['pagina']
