from django.db import models

# models sao os modelos de tabelas que vao compor nosso banco de dados
# sempre devemos registrar nossos novos Models no admin.py (importando a model e registrando admin.site.register(NomeDaModel))
#com models devemos sempre dar o comando makemigrations e em seguida o migrate, para salvar as alterações no banco de dados!!!!!

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2) # maximo de digitos no input e quantas casas depois da virgula
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True) # quer dizer que esse campo nao é obrigatório (null=True, blank=True)
    
    class Meta():
        verbose_name_plural = 'Transações'
        
    def __str__(self):
        return self.descricao 
    # definindo como queremos exibir o dado de cada objeto da nossa classe (que no caso é Transaçao,descriçao)
    # se nao definirmos isso, no navegador aparecerá Transaçao object 1, ao inves de aparecer...
    # o nome da variavel de cada objeto que criamos dentro da nossa classe transaçao que são: data, descriçao e etc...
