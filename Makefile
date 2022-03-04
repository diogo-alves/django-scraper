PACKAGE_MANAGER = poetry
RUNNER = ${PACKAGE_MANAGER} run


## @ Help
.PHONY: help
help: ## Exibe esta lista de comandos
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


## @ Dependencies
.PHONY: install
install: ## Instala as dependências do projeto
	@ echo "Instalando dependências do projeto..."
	${PACKAGE_MANAGER} install


## @ Utils
.PHONY: secret-key
secret-key: ## Gera uma chave secreta para configuração do django
	@ ${RUNNER} python -c "print(__import__('secrets').token_urlsafe())"
	@ echo '----------------------------------------------------------------'
	@ echo "Copie a chave gerada e cole na variável 'DJANGO_SECRET_KEY' em seu arquivo .env"


## @ Local
.PHONY: local local-run local-migrate
local-run: ## Executa aplicação localmente
	@ echo "Execut..."
	${RUNNER} python manage.py runserver
local-migrate: ## Executa migrações do banco de dados localmente
	@ echo "Executando migração do banco de dados..."
	${RUNNER} python manage.py migrate
local: local-migrate local-run ## Executa aplicação e migrações do banco de dados localmente

## @ Executa o scrapy localmente
.PHONY: local-scrape
local-scrape: ## Inicia raspagem de dados localmente
	@ echo "Iniciando raspagem de dados..."
	@ ${RUNNER} scrapy crawl proxies

## @ Docker
.PHONY: docker-up docker-migrate docker-down docker
docker-up: ## Cria e inicia todos os serviços do docker-compose.yml
	@ echo "Iniciando serviços docker..."
	docker-compose up -d
docker-migrate: ## Executa as migrações do banco de dados no docker
	@ echo "Executando migrações..."
	docker-compose exec web python manage.py migrate
docker-down: ## Interrompe os serviços docker
	@ echo "Parando serviços docker..."
	docker-compose down
docker: docker-up docker-migrate ## Executa aplicação e migrações no docker

## @ Executa o scrapy no docker
.PHONY: docker-scrape
docker-scrape: ## Inicia raspagem de dados no docker
	@ echo "Iniciando raspagem de dados..."
	docker-compose exec web scrapy crawl proxies

## @ Linters
.PHONY: linters
lint: ## Executa linters
	@ echo "Executando linters..."
	${RUNNER} pre-commit run --all-files


## @ Tests
.PHONY: tests-local tests-docker
tests-local: ## Executa testes localmente
	@ echo "Executando testes..."
	${RUNNER} pytest .
tests-docker: ## Executa testes no docker
	@ echo "Executando testes..."
	docker-compose exec web pytest .
