from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializersTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            data_lancamento='2003-07-04',
            tipo="F",
            likes=234,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)  

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data  # Corrigido para acessar a propriedade `data`
        self.assertEqual(set(data.keys()), {'titulo', 'tipo', 'data_lancamento', 'likes' })  # Usando conjunto corretamente

    def test_verifica_conteudo_dos_campos_serializados(self):
        """ Teste que verifica o conteudo dos campos serializados """
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)

        ##forçando erro, pois nao tem esse serialize
        #self.assertEqual(data['dislikes'], self.programa.dislikes)

