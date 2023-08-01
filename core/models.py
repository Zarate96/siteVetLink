from django.db import models
from django.utils import timezone
#from ckeditor.fields import RichTextField
from django.utils.text import slugify

SECCIONES  = (
    ('Video', 'Video'),
    ('Accordeon', 'Accordeon'),
    ('Cuadros', 'Cuadros'),
    ('Contacto', 'Contacto'),
    ('Recomendaciones', 'Recomendaciones'),
)

SECCIONES_ID  = (
    ('inicio', 'inicio'),
    ('proceso', 'proceso'),
    ('video', 'video'),
    ('contacto', 'contacto'),
)

class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    is_answered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return f"Mensaje enviado por {self.email} el día {self.fecha}, respondido: {self.is_answered} "

class NavBar(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(verbose_name='icono', upload_to='assets/models/iconos/',)
    fecha = models.DateTimeField(default=timezone.now, editable = False,)

    class Meta:
        verbose_name_plural = "NavBar"

    def __str__(self):
        return f"{self.nombre}"
    
class Secciones(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de sección', choices=SECCIONES, unique=True,)
    titulo = models.TextField(verbose_name='Texto principal',)
    descripcion = models.TextField(verbose_name='Descripción',)
    fecha = models.DateTimeField(default=timezone.now, editable = False,)
    #orden = models.IntegerField(verbose_name='Orden en landing page',)
    #color = models.CharField(max_length=100, v)

    class Meta:
        verbose_name_plural = "Secciones"

    def __str__(self):
        return f"{self.nombre}"

class ElementosNavBar(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(verbose_name='Texto principal', max_length=200,)
    is_button = models.BooleanField(default=False, verbose_name='¿Es botón?',)
    link = models.CharField(max_length=100, verbose_name='Link', blank=True, help_text="Si es butón agrega link externo, si es sección agrega el id de la sección.")
    orden = models.IntegerField(verbose_name='Orden en navbar',)
    seccion_id = models.CharField(max_length=100, verbose_name='Nombre de sección', choices=SECCIONES_ID, blank=True,)
    navbar_id = models.ForeignKey(NavBar, on_delete=models.CASCADE,)
    fecha = models.DateTimeField(default=timezone.now, editable = False,)

    class Meta:
        verbose_name_plural = "ElementosNavBar"

    def __str__(self):
        return f"{self.nombre}"
    
class Slide(models.Model):
    nombre = models.CharField(max_length=100, default="")#quit default al reiniciar bd
    titulo = models.TextField(verbose_name='Título',)
    subtitulo = models.TextField(verbose_name='Subtítulo',)
    texto = models.TextField(verbose_name='Texto del slide',)
    boton_1 = models.CharField(max_length=50, verbose_name='Botón 1',)
    boton_2 = models.CharField(max_length=50, verbose_name='Botón 2',)
    #imagen = models.ImageField(verbose_name='imagen', upload_to='assets/models/Slide/',)
    fecha = models.DateTimeField(default=timezone.now, editable = False,)

    class Meta:
        verbose_name_plural = "Slide"

    def __str__(self):
        return f"{self.titulo} subido el día {self.fecha}"
    
class CuadrosItems(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del cuadro',)
    texto = models.TextField()
    icono = models.ImageField(verbose_name='icono', upload_to='assets/models/iconos/',)
    fecha = models.DateTimeField(default=timezone.now)
    seccion_id = models.ForeignKey(Secciones, on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural = "Cuadros Items"

    def __str__(self):
        return f"{self.nombre} subido el día {self.fecha}"

class AccordeonsItems(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del accordeon',)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    icono = models.ImageField(verbose_name='icono', upload_to='assets/models/iconos/',)
    seccion_id = models.ForeignKey(Secciones, on_delete=models.CASCADE,)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Accordeons Items"

    def __str__(self):
        return f"{self.titulo} subido el día {self.fecha}"

class ContactoItems(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(blank=True)
    icono = models.ImageField(verbose_name='icono', upload_to='assets/models/iconos/',)
    link = models.CharField(max_length=100, verbose_name='Link', blank=True, help_text="Si es necesario enviar a otro sitio como Google Maps.")
    is_required = models.BooleanField(default=False, verbose_name='¿Es requerido?',)
    placeholder = models.CharField(max_length=100, verbose_name='Placeholder', blank=True,)
    order= models.IntegerField(verbose_name='Orden en sección', default=0,)
    seccion_id = models.ForeignKey(Secciones, on_delete=models.CASCADE,)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Contacto Items"

    @property
    def has_link(self):
        return True if self.link else False    
    
    def __str__(self):
        return f"{self.titulo} subido el día {self.fecha}"

class Videos(models.Model):
    titulo = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='assets/models/videos/',)
    thumbnail = models.ImageField(upload_to='assets/models/thumbnails/',)
    fecha = models.DateTimeField(auto_now_add=True)
    seccion_id = models.ForeignKey(Secciones, on_delete=models.CASCADE,)

    def __str__(self):
        return self.titulo