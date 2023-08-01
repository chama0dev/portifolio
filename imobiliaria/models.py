from django.db import models

class Pessoa_Fisica(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    cpf = models.IntegerField(blank=False)
    email = models.EmailField(max_length=254,blank=False)
    celular = models.CharField(max_length=11,blank=False)

class Pessoa_Juridica(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    cnpj = models.IntegerField(blank=False)
    email = models.EmailField(max_length=254,blank=False)
    celular = models.CharField(max_length=11,blank=False)

class Produto(models.Model):
    CATEGORIAS_CHOICES = (
        ('apartamento','Apartamento'),
        ('casa','Casa'),
        ('lote','Lote'),
        ('rural','Rural'),
        ('comercial','Comercial'),
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tamanho = models.DecimalField(max_digits=5, decimal_places=2)
    quarto = models.PositiveIntegerField(blank=True, null=True)
    banheiro = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=200)
    garagem = models.BooleanField(blank=True)
    #imagens = models.ImageField(upload_to='produtos/')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    
    def save(self, *args, **kwargs):
        if self.categoria == 'lote' or self.categoria == 'rural' or self.categoria == 'comercial':
            self.quarto = None
            self.banheiro = None
            self.garagem = None
        super(Produto, self).save(*args, **kwargs)

