from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    site = models.URLField(blank=True)
    interesse = models.IntegerField(default=1, help_text="Nível de interesse de 1 a 5")
 
    class Meta:
        verbose_name_plural = "Tecnologias"
 
    def __str__(self):
        return self.nome
    
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, blank=True)
    nivel = models.IntegerField(default=1, help_text="Nível de proficiência")
 
    class Meta:
        verbose_name_plural = "Competências"
 
    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
 
    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"
        ordering = ['-data_inicio']
 
    def __str__(self):
        return f"{self.nome} — {self.instituicao}"
 
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    pagina = models.URLField(blank=True)
 
    class Meta:
        verbose_name_plural = "Docentes"
 
    def __str__(self):
        return self.nome
    
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    duracao = models.PositiveIntegerField(help_text="Duração em anos")
    instituicao = models.CharField(max_length=200)
    ano_inicio = models.DateField()
    ano_fim = models.DateField(blank=True, null=True)
 
    class Meta:
        verbose_name_plural = "Licenciaturas"
 
    def __str__(self):
        return f"{self.nome} — {self.instituicao}"
 
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=500, blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = "Unidade Curricular"
        verbose_name_plural = "Unidades Curriculares"
 
    def __str__(self):
        return f"{self.codigo} — {self.nome}"
  
class TFC(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000, blank=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    classificacao = models.FloatField(blank=True, null=True)
    licenciatura = models.OneToOneField(Licenciatura, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"
 
    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    competencias = models.ManyToManyField(Competencia, blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link_github = models.URLField(blank=True)
 
    class Meta:
        verbose_name_plural = "Projetos"
 
    def __str__(self):
        return self.nome
class MakingOf(models.Model):
    entidade = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000, blank=True)
    documentacao = models.FileField(upload_to='makingof/', blank=True, null=True)
    decisoes_tomadas = models.TextField(blank=True)
    erros_correcoes = models.TextField(blank=True)
 
    class Meta:
        verbose_name = "Making Of"
        verbose_name_plural = "Making Ofs"
 
    def __str__(self):
        return self.entidade