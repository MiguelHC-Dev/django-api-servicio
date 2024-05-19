from django.contrib import admin
from .models import Usuario, Carrera, TiposFormatos, Formato, ServicioSocial
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
admin.site.register(TiposFormatos)
admin.site.register(Formato)
admin.site.register(ServicioSocial)
admin.site.register(Carrera)

class UsuarioAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'tipo_usuario', 'carrera')}),
        ('Permisos', {'fields': ('servicio', 'residencia', 'ingles')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'first_name', 'last_name', 'email', 'tipo_usuario', 'carrera', 'servicio', 'residencia', 'ingles')}
        ),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'carrera', 'servicio', 'residencia', 'ingles')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('tipo_usuario', 'carrera', 'servicio', 'residencia', 'ingles')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if 'password' in form.cleaned_data:
                obj.set_password(form.cleaned_data['password'])
            obj.save()

admin.site.register(Usuario, UsuarioAdmin)

admin.site.unregister(Group)

