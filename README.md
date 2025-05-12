# processo completo para execução e teste
Este guia descreve o processo de instalação, build e execução de um ambiente Docker com três serviços principais: `db` (MySQL), `api` (FastAPI ou similar) e `test` (Pytest).
---
```
## 1. Instale o Docker e o Docker Compose

### Windows/Mac
- Baixe e instale o **Docker Desktop**:  
  👉 https://www.docker.com/products/docker-desktop/

### Linux (Ubuntu/Debian)

sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker


## 2. Baixe os arquivos para a sua maquina
obs: apesar de ser uma má prática vou sobir o arquivo .env para facilitar o processo de teste.

##  3. Na raiz do projeto você executará os comandos
Certifique-se de estar no diretório raiz do seu projeto, onde está localizado o arquivo `docker-compose.yml`. A partir daí, você poderá executar todos os comandos descritos nas etapas seguintes.

## 4. Build da imagem

Para construir as imagens definidas no `docker-compose.yml`, execute:

```bash
docker-compose build

obs: certifique-se de que está com o programa da docker rodando

##5 Inicie rodando o banco de dados

docker-compose up db

##6  agora podemos subir a nossa api

docker-compose up api

obs: caso não esteja conseguindo acesso ao teclado utilize cntr+c para parar

##6  para finalizar subiremos o teste

docker-compose up test

## ambiente setado
para finalizar utilize o programa docker para iniciar o db, após isso podemos utilizar a nossa api e
checar seu funcionamento no "https://localhost:8000/docs" e quando quiser realizar o teste pode roda-lo,
pois agora o db e banco já estão funcionais.

