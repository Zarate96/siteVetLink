from django.contrib import admin
from .models import Mensajes, NavBar, ElementosNavBar, Slide, Secciones, CuadrosItems, AccordeonsItems, ContactoItems, Videos

@admin.register(Mensajes)
class MensajesAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','empresa','email','fecha','is_answered')

@admin.register(ContactoItems)
class ContactoItemsAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','fecha')

@admin.register(CuadrosItems)
class CuadrosItemsAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fecha')

@admin.register(AccordeonsItems)
class AccordeonAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fecha')

@admin.register(NavBar)
class NavBarAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fecha')

@admin.register(ElementosNavBar)
class ElementosNavBarAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fecha')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','fecha')

@admin.register(Secciones)
class SeccionesAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fecha')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','fecha')
