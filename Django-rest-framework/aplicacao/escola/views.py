# from django.http import JsonResponse

# # Create your views here.
# def alunos(request):
#   if request.method == 'GET':
#     aluno = {
#       "id"  : 1,
#       "nome": "Matheus",
#     }

#     return JsonResponse(aluno)

from rest_framework    import viewsets, generics
from escola.models     import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
  """
    Exibe todos os alunos e alunas
  """ 
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
  """
    Exibe todos os Cursos
  """

  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
  """
    Listando  todas as matrículas
  """ 
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """ 
      Listando as matrículas de aluno ou aluna
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """
      Listando alunos e alunas matriculados em um curso
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
