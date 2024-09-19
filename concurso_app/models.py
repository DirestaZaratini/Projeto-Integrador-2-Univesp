from django.db import models


class Concurso(models.Model):
    numero_processo = models.CharField(max_length=50)
    area_concurso = models.CharField(max_length=100)
    orgao_realizador = models.CharField(max_length=100)
        
    def __str__(self):
        return f"Concurso {self.numero_processo} - {self.area_concurso}"


class Examinador(models.Model):
    nome = models.CharField(max_length=100)
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, related_name='examinadores')
  
    def __str__(self):
        return self.nome


class Prova(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, related_name='provas')
    nome = models.CharField(max_length=100)
    eliminatoria = models.BooleanField(default=False)
    peso = models.FloatField()
    num_pessoas = models.IntegerField()

    def __str__(self):
        return f"Prova {self.nome} - {self.concurso.numero_processo}"


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE, related_name='candidatos')

    def __str__(self):
        return self.nome


class Nota(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='notas')
    examinador = models.ForeignKey(Examinador, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"Nota de {self.candidato} por {self.examinador}"

