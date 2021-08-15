# Busca Cep <img src="https://user-images.githubusercontent.com/37151367/129491645-c2f1763c-23fb-4675-ba7f-1bce38d07e80.jpeg" width="50px" height="40px"> 

<p align="center">
O Busca Cep é uma aplicação desevolvida com objetivo de pesquisar e salvar ceps públicos em um banco de dados, também é possível buscar os ceps salvos ou excluí-los
  
Estou feliz de ter essa oportunidade e desenvolver o sistema para um teste técico para a Claro
  
</p>
<div align="center">
  <sub> Made with 💖 by
    <a href="https://github.com/Escollhas/save_a_brazilian_cep">Matheus Herique Costa
  </sub>
</div>

# Quick start

$ git clone git@github.com:Escollhas/save_a_brazilian_cep.git && cd save_a_brazilian_cep


# Criar ambiente virtual para instalar dependencias
$ python3 -m venv venv | python -m venv venv

# Entrar no ambiente virtual
$ source venv/bin/activate

# Instalar Dependencias
$ pip install -r requirements.txt

# Inicializar o banco de dados dentro da aplicação com flask migrate
$ flask db upgrade
