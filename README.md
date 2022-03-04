# Django-Scraper

 [![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/diogo-alves/django-scraper/blob/main/LICENSE)

Aplicação django que extrai dados de proxies gratuitos disponíveis no site [hidemy.name](https://hidemy.name/en/proxy-list/).


## Preview

Este projeto está disponível para acesso no [Heroku](https://django-proxies-scraper.herokuapp.com/proxies).
[![django-proxies-scraper](https://i.imgur.com/lECrDu0.png)](https://django-proxies-scraper.herokuapp.com/proxies)


## Iniciando

### Pré-requisitos

- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker-compose](https://docs.docker.com/compose/install/)
- [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Make](https://www.gnu.org/software/make/)¹

¹ **NOTA**: A maioria das distribuições linux já disponibilizam o `Make` por padrão. Clique [aqui](http://gnuwin32.sourceforge.net/packages/make.htm) para baixar a versão para Windows.

### Configuração

1. Clone este repositório:

```shell
git clone git@github.com:diogo-alves/django-scraper.git
```

2. Acesse a pasta do repositório:

```shell
cd django-scraper
```

3. Instale as dependências do projeto:

```shell
make install
```

4. Copie o arquivo```.env.example```  e renomeie sua cópia para ```.env```¹ . Para gerar o valor da variável DJANGO_SECRET_KEY execute:

```shell
make secret-key
```
¹ DICA: <small>Para rodar a aplicação localmente usando o `SQLite`, basta comentar a variável `DATABASE_URL`.</small>

## Executando o Projeto

### Localmente

```shell
make local
```

### Com o Docker

```shell
make docker
```

### Testes

```shell
make tests-local
```
ou
```shell
make tests-docker
```

## Raspagem de Dados

```shell
make local-scrape
```
ou

```shell
make docker-scrape
```


## Testes

```shell
make tests-local
```
ou

```shell
make tests-docker
```


## Outros Comandos disponíveis

Para ver a lista de todos os comandos utilitários disponíveis:
```shell
make help
```

## Licença

Este projeto está sob os termos da licença [MIT](./LICENSE).
