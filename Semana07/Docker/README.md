### Configuração do Mongo e Docker

1. Nosso primeiro passo é garantir a instalação do docker desktop no computador (https://www.docker.com/products/docker-desktop/).

2.  Obter a imagem do Mongo que será o molde para criarmos nossos containers. Para isso, executamos o comando abaixo.

```(Bash)
docker pull mongo
```

3. Para executar esta imagem você pode usar a linha abaixo. 

```(Bash)
docker run --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo
```

4. Instale a extensão MongoDB for VS Code. 

5. Acesse a extensão (uma folha na barra lateral), clique em Add Connection e use as configurações:

```(Bash)
mongodb://root:root@localhost:27017/admin
```

Mais detalhes em: https://balta.io/blog/mongodb-docker