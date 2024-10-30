from django.db import models

class client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField()
    altura = models.DecimalField(max_digits=2, decimal_places=2)
    peso = models.DecimalField(max_digits=3, decimal_places=2)
    Atividade = models.TextField()

class receita(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField()
    tempo = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.nome

class valores_nutricionais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField()
    gordura = models.DecimalField(max_digits=2, decimal_places=2)
    carboidrato = models.DecimalField(max_digits=2, decimal_places=2)
    proteina = models.DecimalField(max_digits=2, decimal_places=2)
    porção = models.DecimalField(max_digits=2, decimal_places=2)
    unidade = models.TextField()

class utensilio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField()
    
class favoritado(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_Receita = models.ForeignKey(receita, on_delete=models.CASCADE)
    id_Cliente = models.ForeignKey(client, on_delete=models.CASCADE)

class ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_receita = models.ForeignKey(receita, on_delete=models.CASCADE)
    id_val_Nutri = models.ForeignKey(valores_nutricionais, on_delete=models.CASCADE)
    quant = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    unidade = models.TextField()

class receita_utensilio(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_receita = models.ForeignKey(receita, on_delete=models.CASCADE)
    id_utensilio = models.ForeignKey(utensilio, on_delete=models.CASCADE)



