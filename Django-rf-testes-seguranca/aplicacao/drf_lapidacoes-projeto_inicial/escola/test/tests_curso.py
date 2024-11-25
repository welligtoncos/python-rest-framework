from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
import json

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2', nivel = 'B'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito!')

    def test_requisicao_get_listar_cursos(self):
        """ 
        Teste para verificar se a requisição GET para listar os cursos
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




    def test_create_curso(self):
        """
        Teste para criar um novo curso via POST request.
        """
        data = {
            "codigo_curso": "PYT101",
            "descricao": "Curso de Python Básico",
            "nivel": "B"
        }
        response = self.client.post(
        self.list_url,
        data=json.dumps(data),  # Serializa os dados para JSON
        content_type='application/json'
        )
        #print(response.json())  # Para verificar a resposta detalhada
 
        # Verificando se o status da resposta está correto (201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        
        # Cria um curso antes de tentar deletar
        curso = Curso.objects.create(
            codigo_curso="CTT3",
            descricao="Curso teste 3",
            nivel="A"
        )
        
        # Tenta deletar o curso
        response = self.client.delete(f'/cursos/{curso.id}/')
        
        # Verifica se o status retornado é 405 Method Not Allowed
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
   
 
    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar requisição PUT para atualizar um curso"""
        
        # Cria um curso antes de tentar atualizá-lo
        curso = Curso.objects.create(
            codigo_curso="CTT1",
            descricao="Curso teste 1",
            nivel="A"
        )
        
        # Dados atualizados para a requisição PUT
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso teste 1 atualizado',
            'nivel': 'I'
        }
        
        # Executa a requisição PUT para atualizar o curso, convertendo os dados para JSON
        response = self.client.put(f'/cursos/{curso.id}/', data=json.dumps(data), content_type='application/json')
        
        # Imprime a resposta para depuração
        #print("Resposta da API:", response.json())
        
        # Verifica se o status retornado é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
