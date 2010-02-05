from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField

PROFILE_SIZES = ((100, 100),
         (150, 150),
         (75, 75),
         (300, 200),
        )

class Area(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    
    class Meta:
        verbose_name_plural = "Areas"
        
    def __unicode__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name = "Usuario")
    cargo = models.CharField(max_length = 50)
    extension = models.PositiveIntegerField(max_length=3)
    area = models.ForeignKey(Area)
    celular = models.CharField(max_length=20, blank=True) 
    skype = models.CharField(max_length=25, blank=True) 
    casa = models.CharField(max_length=20, blank=True) 
    avatar = ImageWithThumbsField(upload_to='images/profile', sizes=PROFILE_SIZES)

    def get_absolute_url(self):
        return '/perfiles/%s/' % self.user.username

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = 'perfiles'

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def __unicode__(self):
        return self.nombre
        
class Link(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.URLField()
    peso = models.IntegerField()
    categoria = models.ForeignKey(Categoria)

    class Meta:
        verbose_name_plural = "Links"
        
    def __unicode__(self):
        return self.nombre

class Archivo(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    adjunto = models.FileField(upload_to='attachments/documentos')
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(UserProfile)
	
    def get_absolute_url(self):
    	return '%s%s/%s' % (settings.MEDIA_URL, settings.ATTACHMENT_FOLDER, self.id)

    def get_download_url(self):
    	return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    class Meta:
    	verbose_name_plural = "Subir Archivos"

    def __unicode__(self):
    	return self.titulo
		
class DiasFeriados(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural="Dias Feriados"
        
    def __unicode__(self):
        return self.descripcion
        
class Noticia(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=50)
    texto = models.TextField(default=" ")
    destacado = models.BooleanField()
    autor = models.ForeignKey(UserProfile)
    
    class Meta:
        verbose_name_plural = "Noticias"
        
    def __unicode__(self):
        return self.titulo
        
class Actividad(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=50)
    area = models.ForeignKey(Area)
    participantes = models.ManyToManyField(UserProfile)
    
    class Meta:
        verbose_name_plural = "Actividades diarias"
        
    def __unicode__(self):
        return self.evento    
