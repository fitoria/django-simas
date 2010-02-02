from django.contrib import admin
from models import UserProfile

admin.site.register(UserProfile,
                    list_display = ['user', 'skype', 'cargo', 'area', 'celular'],
                    list_filter = ['area'],
                    ordering = ['user', 'area']
                   )
