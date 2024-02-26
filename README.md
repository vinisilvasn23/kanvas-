# API de Gerenciamento de Cursos e Aulas (EAD) - Kanvas

## O Projeto

Desenvolvimento de uma API REST para o gerenciamento de cursos e aulas em um ambiente de ensino a distância (EAD). Foi utilizado Python e o framework Django, juntamente com o Django Rest Framework para construir a aplicação.

## Principais Recursos

- Banco de Dados PostgreSQL
- Documentação no formato Swagger para uma experiência de uso simples
- Deploy da aplicação no Render
- Autenticação com JSON Web Token (JWT)

## Requisitos de Instalação

Antes de começar a usar a API, certifique-se de que possui os seguintes requisitos instalados em seu ambiente:

- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL
- Render (para implantação na web)
- Outras dependências especificadas no arquivo `requirements.txt`
## Configuração e Uso

1. **Clone o repositório:**

   ```shell
   git clone https://github.com/vinisilvasn23/kanvas-

2. **Configure o ambiente virtual:**
```shell
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
```
3. **Instale as dependências:**
```shell
Copy code
pip install -r requirements.txt
Configure o banco de dados:
```

4. **Crie um banco de dados PostgreSQL.**
Atualize as configurações de banco de dados no arquivo settings.py.

5. **Aplicar migrações:**
```shell
Copy code
python manage.py migrate
```
6. **Execute a aplicação:**

```shell
Copy code
python manage.py runserver
```

Acesse a documentação Swagger:

Abra seu navegador e acesse http://localhost:8000/swagger/ para explorar e testar os endpoints da API.

Link do deploy no Render: https://kanvas-lmzh.onrender.com/api/docs/
