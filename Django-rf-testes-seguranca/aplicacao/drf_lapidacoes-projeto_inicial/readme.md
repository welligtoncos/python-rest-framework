2. Iniciar um Contêiner Redis
Após o download da imagem, inicie o contêiner Redis com o comando abaixo:

bash
Copiar código
docker run --name meu-redis -d -p 6379:6379 redis
Explicação do Comando:
--name meu-redis: Nomeia o contêiner como "meu-redis".
-d: Executa o contêiner em segundo plano (modo "detached").
-p 6379:6379: Mapeia a porta 6379 do contêiner para a porta 6379 do host, permitindo acesso ao Redis através do host local.
3. Verificar se o Contêiner Está em Execução
Para confirmar que o contêiner está ativo, execute o comando:

bash
Copiar código
docker ps
Este comando exibe uma lista de contêineres em execução. Verifique se o "meu-redis" está listado entre eles.

4. Conectar-se ao Redis
Para interagir com o Redis, utilize o cliente de linha de comando redis-cli. Se você não o tiver instalado localmente, pode acessá-lo dentro do próprio contêiner:

bash
Copiar código
docker exec -it meu-redis redis-cli
Este comando abre uma sessão interativa do redis-cli conectada ao contêiner Redis em execução.

5. Testar a Conexão
Dentro do redis-cli, teste a conexão com o seguinte comando:

bash
Copiar código
ping
Se a resposta for PONG, significa que o Redis está funcionando corretamente e está pronto para ser utilizado.

Configurar Persistência de Dados (Opcional)
Por padrão, os dados armazenados no Redis dentro de um contêiner Docker não são persistentes. Para garantir que os dados sejam mantidos mesmo após reiniciar ou remover o contêiner, configure um volume com persistência:

bash
Copiar código
docker run --name meu-redis -d -p 6379:6379 -v /caminho/local/para/dados:/data redis redis-server --appendonly yes
Substitua /caminho/local/para/dados pelo caminho no sistema onde deseja armazenar os dados do Redis.
O parâmetro --appendonly yes ativa o modo de persistência AOF (Append Only File) do Redis, que grava cada operação no disco, garantindo que os dados persistam.


Depois de ter colocado docker agora está assim

    docker-compose up



criar a pasta
python manage.py makemessages -l pt_BR -i requirements.txt

ajustar django.po
texto

compilar
python manage.py compilemessages


teste
python manage.py test escola.test.tests_curso


instalação do honeypot
pip install git+https://github.com/dmpayton/django-admin-honeypot.git@develop
