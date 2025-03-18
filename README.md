## Desafio UOL

Este projeto é uma solução para o desafio de backend proposto pela UOL Host, desenvolvido utilizando **Python com Django**.

## Descrição
O desafio consiste em criar um sistema capaz de:
- Recuperar informações de arquivos JSON e XML disponibilizados via URL.
- Permitir o cadastro de jogadores contendo nome, e-mail e telefone.
- Persistir os dados cadastrados em um banco de dados em memória.
- Listar os jogadores cadastrados, exibindo suas informações e o arquivo de referência utilizado (JSON ou XML).
- Impedir que um mesmo codinome seja utilizado mais de uma vez dentro da mesma lista.

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/ThalesBergamim/desafio_uol.git
   ```

2. Crie um ambiente virtual, ative-o e instale as dependências:
   ```bash
   python -m venv venv
   pip install -r requirements.txt
   ```

3. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor e acesse-o pelo link:
   ```bash
   python manage.py runserver
   http://127.0.0.1:8000
   ```

## Desafio
O desafio pode ser encontrado no respósitorio: [Desafio UOL](https://github.com/feltex/desafio-uol)


