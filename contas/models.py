from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    livro = models.CharField(max_length=200)
    pag = models.DecimalField(max_digits=6, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=80)
    ano = models.DecimalField(max_digits=4, decimal_places=0)
    

    class Meta:
        verbose_name_plural = 'Cadastro_Livros'

    def __str__(self):
        return self.livro