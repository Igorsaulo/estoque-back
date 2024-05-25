# Estoque Back

Esse projeto complementa o projeto estoque-front que pode ser baixado em:
https://github.com/Igorsaulo/controle-estoque-front

### Executando o projeto:
Para executar é preciso ter o poetry instalando no seu ambiente de desenvolvimento

#### Clone o repósitorio:

```bash
git clone https://github.com/Igorsaulo/estoque-back.git
```
#### Instalando as denpêndencias
```bash
poetry install
```

#### Fazendo as migrações do banco de dados:
```bash
poetry run python manage.py migrate
```
#### Populando seu banco com produtos de amostra:
```bash
poetry run python manage.py seed_products
```

#### Iniciando o servidor:
```
poetry run python manage.py runserver
```

#### Acesse a documentação da API em:
http://127.0.0.1:8000/api/doc/