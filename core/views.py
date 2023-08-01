from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .decorators import check_recaptcha
from .models import Mensajes, NavBar, ElementosNavBar, Slide, Secciones, CuadrosItems, AccordeonsItems, ContactoItems, Videos

# Create your views here.

class Inicio(UserPassesTestMixin, TemplateView):
    template_name = 'core/home.html'

    def test_func(self):
        return True
        
    def get_context_data(self, *args, **kwargs):
        navbar = NavBar.objects.all().first()
        navbar_items = ElementosNavBar.objects.all().order_by('orden')
        slide = Slide.objects.all().first()
        seccion_cuadros = Secciones.objects.get(nombre='Cuadros')
        seccion_accordeons = Secciones.objects.get(nombre='Accordeon')
        seccion_video_principal = Secciones.objects.get(nombre='Video')
        video_seccion_principal = Videos.objects.filter(seccion_id=seccion_video_principal).first()
        seccion_recomendaciones = Secciones.objects.get(nombre='Recomendaciones')
        cuadros = CuadrosItems.objects.all()
        accordeons = AccordeonsItems.objects.all()
        contacto = Secciones.objects.get(nombre='Contacto')
        contacto_items = ContactoItems.objects.filter(seccion_id=contacto).order_by('order')

        context = super().get_context_data(*args,**kwargs)
        context['title'] = 'Inicio'
        context['navbar'] = navbar
        context['navbar_items'] = navbar_items
        context['slide'] = slide
        context['seccion_cuadros'] = seccion_cuadros
        context['seccion_accordeons'] = seccion_accordeons
        context['seccion_video'] = seccion_video_principal
        context['video_seccion_principal'] = video_seccion_principal
        context['seccion_recomendaciones'] = seccion_recomendaciones
        context['cuadros'] = cuadros
        context['accordeons'] = accordeons
        context['contacto'] = contacto
        context['contacto_items'] = contacto_items
        context['google_site_key'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
        return context
    
@check_recaptcha
def mensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        empresa = request.POST['empresa']
        email = request.POST['email']
        mensaje = request.POST['mensaje']

    if request.recaptcha_is_valid:    
        mensaje = Mensajes(nombre=nombre, empresa=empresa, email=email, mensaje=mensaje)
        mensaje.save()
        messages.success(request, 'Tu mensaje ha sido enviado, nos pondremos en contacto contigo en breve.')

    else:
        messages.error(request, 'Porfavor verifique la información')

    return redirect(request.META['HTTP_REFERER'])
    #return render(request, 'pages/home.html', {})