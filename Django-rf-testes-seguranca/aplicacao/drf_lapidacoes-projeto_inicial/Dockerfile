# Use a imagem oficial do Python como base
FROM python:3.9

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências (requirements.txt) para o container
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório atual para o diretório de trabalho no container
COPY . /app/

# Expõe a porta 8000 para que possamos acessar o Django externamente
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
