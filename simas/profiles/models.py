from django.db import models
from django.contrib.auth.models import User
from simas.pagina.models import Area
from thumbs import ImageWithThumbsField

SIZES = ((100, 100),
         (150, 150),
         (75, 75),
         (300, 200),
        )
class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name = "Usuario")
    cargo = models.CharField(max_length = 50)
    extension = models.PositiveIntegerField(max_length=3)
    area = models.ForeignKey(Area)
    celular = models.CharField(max_length=20, blank=True) 
    skype = models.CharField(max_length=25, blank=True) 
    casa = models.CharField(max_length=20, blank=True) 
    avatar = ImageWithThumbsField(upload_to='images/profile', sizes=SIZES)

    def get_absolute_url(self):
        return '/perfiles/%s/' % self.user.username

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = 'perfiles'
