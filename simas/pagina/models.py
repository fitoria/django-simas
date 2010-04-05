 # -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
from django.conf import settings

PROFILE_SIZES = ((100, 100),
         (150, 150),
         (75, 75),
         (300, 200),
        )

class Area(models.Model):
    nombre = models.CharField(max_length = 25, unique = True)
    
    class Meta:
        verbose_name_plural = "Areas"
        
    def __unicode__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name = "Usuario")
    cargo = models.CharField(max_length = 50)
    extension = models.PositiveIntegerField(max_length = 3)
    area = models.ForeignKey(Area)
    celular = models.CharField(max_length = 20, blank = True) 
    skype = models.CharField(max_length = 25, blank = True)
    fecha = models.DateField('Fecha de nacimiento', blank = True, 
                             null = True, help_text = "Año-Mes-Dia (2010-12-28)") 
    casa = models.CharField("Telefono de casa", max_length = 20, blank = True) 
    avatar = ImageWithThumbsField('Foto', upload_to = 'profile/', 
                                  sizes = PROFILE_SIZES,
                                  help_text = "Subir su fotografia personal")

    def get_absolute_url(self):
        return '/perfiles/%s/' % self.user.username

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = 'perfiles'

class Categoria(models.Model):
    nombre = models.CharField(max_length = 25, unique = True)
    slug = models.SlugField(max_length = 25, unique = True, 
                            help_text = 'Unico valor')
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def __unicode__(self):
        return self.nombre

class Seccion(models.Model):
    nombre = models.CharField(max_length = 25, unique = True, 
                              blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True, 
                            help_text = 'unico Valor')

    class Meta:
        verbose_name_plural = "Seccion"
        
    def __unicode__(self):
        return self.nombre
        
class Subseccion(models.Model):
    nombre = models.CharField(max_length = 25, unique = True, 
                              blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True, 
                            help_text = 'unico Valor')
    seccion = models.ForeignKey(Seccion)
    
    class Meta:
        verbose_name_plural = "Subsecciones"
        ordering = ['seccion']
        
    def __unicode__(self):
        return "%s - %s" % (self.nombre, self.seccion.nombre)
       
class Link(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)
    direccion = models.URLField()
    peso = models.IntegerField()
    categoria = models.ForeignKey(Categoria)

    class Meta:
        verbose_name_plural = "Links"
        ordering = ['peso']
        
    def __unicode__(self):
        return self.nombre

class Archivo(models.Model):
    titulo = models.CharField(max_length = 200)
    fecha = models.DateField()
    descripcion = models.TextField(blank = True, null = True)
    adjunto = models.FileField(upload_to = 'attachments/documentos')
    adjunto1 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto2 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto3 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto4 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    subseccion = models.ForeignKey(Subseccion) 
    usuario = models.ForeignKey(UserProfile)
	
    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, 
                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Subir Archivos"

class DiasFeriados(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name_plural = "Dias Feriados"
        
    def __unicode__(self):
        return self.descripcion
        
class Noticia(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length = 50)
    texto = models.TextField(default = " ")
    autor = models.ForeignKey(UserProfile)
    
    class Meta:
        verbose_name_plural = "Noticias"
        ordering = ('-fecha', '-id',)
        
    def __unicode__(self):
        return self.titulo
        
class Actividad(models.Model):
    fecha = models.DateTimeField()
    titulo = models.CharField(max_length = 150)
    descripcion = models.TextField(default = "")
    lugar = models.CharField(max_length = 50)
    area = models.ForeignKey(Area)
    participantes = models.ManyToManyField(UserProfile)
    
    class Meta:
        verbose_name_plural = "Actividades diarias"
        ordering = ('-fecha', 'titulo')
        
    def __unicode__(self):
        return self.titulo
        
class Organizacion(models.Model):
    nombre = models.CharField(max_length = 100, unique = True)
    descripcion = models.TextField(blank = True, null = True)
    
    class Meta:
        verbose_name_plural = "Organizaciones"
        
    def __unicode__(self):
        return self.nombre
            
class TipoContacto(models.Model):
    nombre = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name_plural = "Tipos de Contactos"
    
    def __unicode__(self):
        return self.nombre
        
class Pais(models.Model):
    nombre = models.CharField(max_length = 45, unique = True)
    slug = models.SlugField(max_length = 25, unique = True)
    
    class Meta:
        verbose_name_plural = "Paises"
        
    def __unicode__(self):
        return self.nombre  
        
class Contacto(models.Model):
    profesion = models.CharField(max_length = 50, blank = True, 
                                 null = True)
    nombres = models.CharField(max_length = 75)
    apellidos = models.CharField(max_length = 75)
    organizacion = models.ForeignKey(Organizacion)
    email1 = models.EmailField(blank = True, null = True)
    email2 = models.EmailField(blank = True, null = True)
    skype = models.CharField(max_length=30, blank = True, 
                             null = True)
    tel1 = models.CharField('Telefono 1', max_length = 40)
    tel2 = models.CharField('Telefono 2', max_length = 40, blank = True, 
                               null = True)
    tel3 = models.CharField('Telefono 3', max_length = 40, blank = True, 
                               null = True)
    fax = models.CharField('Fax', max_length = 40, blank = True, null = True)
    cel1 = models.CharField('Celular 1', max_length = 40,blank = True, 
                               null = True)
    cel2 = models.CharField('Celular 2', max_length = 40, blank = True, 
                               null = True)
    dir1 = models.TextField('Direccion 1', blank = True, 
                            null = True)
    dir2 = models.TextField('Direccion 2', blank = True, 
                            null = True)
    ciudad = models.CharField(max_length=60, blank = True, 
                              null = True)
    codigo = models.CharField('Codigo Postal', 
                              max_length = 40, blank = True, 
                              null = True)
    pais = models.ForeignKey(Pais, blank=True, null = True)
    tipo = models.ForeignKey(TipoContacto, blank = True, 
                             null = True)
    comentario = models.TextField(blank = True, null = True)
    sitio = models.URLField('Sitio Web', blank = True, 
                            null = True, help_text = "Introduzca el sitio asi: http://www.sitio.com")
    
    
    class Meta:
        verbose_name_plural = "Contactos"
    
    def __unicode__(self):
        return self.nombres
