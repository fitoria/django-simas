from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def __unicode__(self):
        return self.nombre
        
class Area(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    
    class Meta:
        verbose_name_plural = "Area"
        
    def __unicode__(self):
        return self.nombre

class Links(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.URLField()
    peso = models.IntegerField()
    categoria = models.ForeignKey(Categorias)

    class Meta:
        verbose_name_plural = "Links"
        
    def __unicode__(self):
        return self.nombre

class Subir_archivos(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    adjunto = models.FileField(upload_to='attachments/documentos')
    categoria = models.ForeignKey(Categorias)
	
    def get_absolute_url(self):
    	return '%s%s/%s' % (settings.MEDIA_URL, settings.ATTACHMENT_FOLDER, self.id)

    def get_download_url(self):
    	return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    class Meta:
    	verbose_name_plural = "Subir Archivos"

    def __unicode__(self):
    	return self.titulo
		
class Dias_feriados(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural="Dias Feriados"
        
    def __unicode__(self):
        return self.descripcion
        
class Noticias(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    Destacado = models.BooleanField()
    usuario = models.ForeignKey(User)
    
    class Meta:
        verbose_name_plural = "Noticias"
        
    def __unicode__(self):
        return self.titulo
        
class Actividades(models.Model):
    fecha = models.DateTimeField()
    evento = models.TextField()
    lugar = models.CharField(max_length=50)
    area = models.ForeignKey(Area)
    
    class Meta:
        verbose_name_plural = "Actividades diarias"
        
    def __unicode__(self):
        return self.evento    
