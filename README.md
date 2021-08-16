# Busca Cep <img src="https://user-images.githubusercontent.com/37151367/129491645-c2f1763c-23fb-4675-ba7f-1bce38d07e80.jpeg" width="50px" height="40px"> 

<p align="center">
O Busca Cep é uma aplicação desenvolvida com objetivo de pesquisar e salvar ceps públicos em um banco de dados, também é possível buscar os ceps salvos ou excluí-los
  
Estou feliz de ter essa oportunidade e poder desenvolver essa aplicação para uma oportunidade dentro da Claro
  
</p>
<div align="center">
  <sub> Made with 💖 by
    <a href="https://github.com/Escollhas/save_a_brazilian_cep">Matheus Herique Costa
  </sub>
</div>

# Passo a passo para rodar o projeto

$ git clone git@github.com:Escollhas/save_a_brazilian_cep.git && cd save_a_brazilian_cep


# Criar ambiente virtual para instalar dependencias
$ python3 -m venv venv | python -m venv venv (Linux)

# Entrar no ambiente virtual
$ source venv/bin/activate

# Instalar Dependencias
$ pip install -r requirements.txt

# Inicializar o banco de dados dentro da aplicação com Flask Migrate
$ flask db upgrade

​
​
​
# Como utilizar o sistema - Busca Cep API RESTFUL

É necessário utilizar um API Client, como o Insomnia, ThunderClient, Postman

# Rodar a aplicação
$ flask run

- Você pode ir para a porta padrão do Flask http://localhost:5000/ para rodar a aplicação.

# Rotas
​
### REGISTRAR CEP - [POST] - "/cep"
​
Ao fazer a requisição a partir de um cep é possível salvar as informações.
​
- **Request**
  - Body
​
```json
{
	"cep": "04117-091"
}
```
​
- **Response**
  - Body
​
```json
{
  "id": 1,
  "cep": "04117-091",
  "logradouro": "Rua Francisco Cruz",
  "complemento": "de 135/136 ao fim",
  "localidade": "São Paulo",
  "bairro": "Vila Mariana",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107",
  "validated": true,
  "created_at": "2021-08-15 23:18:31"
}
```
### DELETAR CEP - [DELETE] - "/cep/<int:cep_id>"
​
Ao fazer a requisição a partir de um cep é possível deletar as informações.
​
- **Request**
  - No Body

​
- **Response**
  - Body
​
```json
{
  "message": "Cep deletado com sucesso"
}
```
### BUSCAR CEP - [GET] - "/cep" ou "/cep/<int:cep_id>"
​
Ao fazer a requisição da rota cep é possível buscar todos os ceps do sistema ou pelo id
​
- **Request**
  - No Body

​
- **Response**
  - Body
​
```json
[
  {
    "id": 1,
    "cep": "04117-091",
    "logradouro": "Rua Francisco Cruz",
    "complemento": "de 135/136 ao fim",
    "localidade": "São Paulo",
    "bairro": "Vila Mariana",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7107",
    "validated": true,
    "created_at": "2021-08-15 23:18:31"
  },
  {
    "id": 2,
    "cep": "02248-001",
    "logradouro": "Rua Cruz de Malta",
    "complemento": "de 681/682 ao fim",
    "localidade": "São Paulo",
    "bairro": "Parada Inglesa",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7107",
    "validated": false,
    "created_at": "2021-08-15 23:44:42"
  },
  {
    "id": 3,
    "cep": "88035-350",
    "logradouro": "Rua João Carlos de Souza",
    "complemento": "",
    "localidade": "Florianópolis",
    "bairro": "Santa Mônica",
    "uf": "SC",
    "ibge": "4205407",
    "gia": "",
    "ddd": "48",
    "siafi": "8105",
    "validated": true,
    "created_at": "2021-08-15 23:44:42"
  }
]
```
  
# Tecnologias utilizadas 📱

- Flask
- Flask Migrate
- SQLAlchemy
- SQLite


Made with 💖 by [Matheus Herique](https://www.linkedin.com/in/matheush-costa/).

