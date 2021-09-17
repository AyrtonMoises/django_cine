from django.db import models
from django.forms import ValidationError


IDADE_INDICATIVA_CHOICES = (
    ('L', 'Livre'),
    ('10', '10 Anos'),
    ('14', '14 Anos'),
    ('16', '16 Anos'),
    ('18', '18 Anos'),
)

CATEGORIA_CHOICES = (
    (1, 'Comédia'),
    (2, 'Terror'),
    (3, 'Sci-fi'),
    (4, 'Ação'),
    (5, 'Infantil'),
    (6, 'Romance'),
    (7, 'Suspense'),
    (8, 'Drama'),
    (9, 'Documentário'),
)

class Filme(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=100)
    sinopse = models.TextField()
    trailer = models.URLField(blank=True, null=True)
    duracao = models.TimeField(verbose_name='Duração')
    dublado = models.BooleanField(default=False)
    legendado = models.BooleanField(default=False)
    formato_2D = models.BooleanField(default=False)
    formato_3D = models.BooleanField(default=False)
    indicacao = models.CharField(
        verbose_name='Indicação', choices=IDADE_INDICATIVA_CHOICES, max_length=10
    )
    categoria = models.PositiveSmallIntegerField(choices=CATEGORIA_CHOICES)
    em_breve = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Sala(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=50)
    ativa = models.BooleanField()

    def __str__(self):
        return self.titulo


class Sessao(models.Model):
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='sala_sessao',
        limit_choices_to={'ativa': True}
    )
    filme = models.ForeignKey(
        Filme,
        on_delete=models.CASCADE,
        related_name='filme_sessao',
        limit_choices_to={'ativo': True}
    )
    data_hora_inicial = models.DateTimeField()
    data_hora_final = models.DateTimeField()
    ativa = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Sessões"
        verbose_name = "Sessão"

    def __str__(self):
        return f'''{self.sala} - Filme: {self.filme} - Data: 
            {self.data_hora_inicial.strftime("%d/%m/%y Horário:%H:%M")}'''

    def clean(self):
        """ Verifica se data final e menor que inicial """
        if self.data_hora_final < self.data_hora_inicial:
            raise ValidationError("Data final da sessão deve ser maior que início")

        """ Verifica se existem sessões no mesmo horário e sala"""
        sessoes_no_periodo = Sessao.objects.filter(
            data_hora_final__gte=self.data_hora_inicial,
            data_hora_inicial__lte=self.data_hora_final,
            sala=self.sala
        ).exclude(pk=self.pk)
        
        if sessoes_no_periodo:
            raise ValidationError("Existem sessões nesse horário e sala!")