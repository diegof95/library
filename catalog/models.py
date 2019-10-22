from django.db import models

class Autor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    class Meta:
        verbose_name_plural = 'autores'
    
    def __str__(self):
        return self.nombre +' '+ self.apellido
    
class Editor(models.Model):
    
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50, blank=True)
    ciudad = models.CharField(max_length=60, blank=True)
    estado = models.CharField(max_length=30, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = 'editores'

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    
    titulo = models.CharField(max_length=100)
    autor = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_pub = models.DateField(null=True, blank=True)
    portada = models.ImageField(upload_to='portadas', blank=True)

    def __str__(self):
        return self.titulo +' - '+ self.autor.__str__()
    
    def get_autor(self):
        
        query_autors = self.autor.all()
        autors = ''
        for autor in query_autors:
            autors += autor.__str__() +', '
        #print(query_autors.len())
        
        return autors
        
    get_autor.short_description = 'Autor'