from django.test import TestCase
from django.forms import ValidationError

from catalogo.models import Filme, Sessao, Sala


class FilmeTestCase(TestCase):

    def setUp(self):
        self.filme = Filme.objects.create(
            titulo = 'Matrix',
            sinopse = 'era uma vez uma sinopse ...',
            trailer = 'www.youtube.com/trailer',
            duracao = '03:30:00',
            dublado = True,
            legendado = True,
            formato_2D = True,
            formato_3D = False,
            indicacao = 1,
            categoria = 3,
            em_breve = False,
            ativo = True
        )

    def test_criar_filme(self):
        """ Criar um filme """
        Filme.objects.create(
            titulo = 'Matrix',
            sinopse = 'era uma vez uma sinopse ...',
            trailer = 'www.youtube.com/trailer',
            duracao = '03:00:00',
            dublado = True,
            legendado = True,
            formato_2D = True,
            formato_3D = False,
            indicacao = 1,
            categoria = 3,
            em_breve = False,
            ativo = True
        )
        self.assertEqual(Filme.objects.count(), 2)

    def test_atualizar_filme(self): 
        """ Atualizar um filme """  
        self.filme.duracao = '01:30:00'
        self.filme.formato_3D = True
        self.filme.save()
        self.assertEqual(self.filme.duracao, '01:30:00')
        self.assertEqual(self.filme.formato_3D, True)
        
    def test_deletar_filme(self):
        """ Deletar um filme """
        self.filme.delete()
        self.assertEqual(Filme.objects.count(), 0)


class SessaoTestCase(TestCase):

    def setUp(self):
        self.filme = Filme.objects.create(
            titulo = 'Matrix',
            sinopse = 'era uma vez uma sinopse ...',
            trailer = 'www.youtube.com/trailer',
            duracao = '03:30:00',
            dublado = True,
            legendado = True,
            formato_2D = True,
            formato_3D = False,
            indicacao = 1,
            categoria = 3,
            em_breve = False,
            ativo = True
        )
        self.salas = Sala.objects.bulk_create(
            [
                Sala(titulo='Sala 1', ativa=True), 
                Sala(titulo='Sala 2', ativa=True)
            ]
        )
        self.sessao = Sessao.objects.create(
            sala = self.salas[0],
            filme = self.filme,
            data_hora_inicial = '2021-09-15 19:00:00',
            data_hora_final = '2021-09-15 20:00:00',
            ativa = True
        )

    def test_criar_sessao(self):
        """ Criar uma sessão """
        self.sessao = Sessao.objects.create(
            sala = self.salas[0],
            filme = self.filme,
            data_hora_inicial = '2021-09-15 15:00:00',
            data_hora_final = '2021-09-15 16:00:00',
            ativa = True
        )
        self.assertEqual(Sessao.objects.count(), 2)

    def test_atualizar_sessao(self): 
        """ Atualizar uma sessão """  
        self.filme.data_hora_final = '2021-09-15 22:00:00'
        self.filme.sala = self.salas[1]
        self.filme.save()
        self.assertEqual(self.filme.data_hora_final, '2021-09-15 22:00:00')
        self.assertEqual(self.filme.sala, self.salas[1])
        
    def test_deletar_sessao(self):
        """ Deletar uma sessão """
        self.filme.delete()
        self.assertEqual(Sessao.objects.count(), 0)

    def test_criar_sessao_no_mesmo_horario(self):
        """ Tentativa de criação de sessão no mesmo horário """
        instancia = Sessao(
            sala = self.salas[0],
            filme = self.filme,
            data_hora_inicial = '2021-09-15 19:30:00',
            data_hora_final = '2021-09-15 21:30:00',
            ativa = True
        )
        self.assertRaises(ValidationError, instancia.clean)

    def test_criar_sessao_com_horario_inicial_maior_que_horario_final(self):
        """
        Tentativa de criação de sessão com horário inicial 
        maior que horário final
        """
        instancia = Sessao(
            sala = self.salas[0],
            filme = self.filme,
            data_hora_inicial = '2021-09-20 19:30:00',
            data_hora_final = '2021-09-15 21:30:00',
            ativa = True
        )
        self.assertRaises(ValidationError, instancia.clean)