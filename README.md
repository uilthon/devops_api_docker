#  API Flask + MySQL com Docker Compose

##  Descrição
Este projeto implementa uma **API REST CRUD** simples utilizando **Flask** (Python) e **MySQL**, executando em um ambiente **multi-container** gerenciado pelo **Docker Compose**.  
A API permite **criar, listar, atualizar e excluir** usuários armazenados no banco de dados.

##  Estrutura do Projeto
```
devops_api_docker/
│
├── app/
│   ├── __init__.py          # Inicialização do app Flask
│   ├── crud.py              # Funções de manipulação no banco
│   ├── main.py              # Endpoints da API Flask
│   └── requirements.txt     # Dependências Python
│
├── init.sql                 # Script inicial do banco (tabela users)
├── Dockerfile               # Build da aplicação Flask
├── docker-compose.yml       # Configuração dos containers
├── .env                     # Variáveis de ambiente (DB_NAME, USER, SENHA)
└── README.md                # Documentação do projeto
```

##  Como Executar no WSL
```bash
cd ~/devops_api_docker
docker compose up -d --build
```
Verifique se os containers estão ativos:
```bash
docker compose ps
```

##  Testes com curl
###  Criar usuário
```bash
curl -X POST http://localhost:5000/users      -H "Content-Type: application/json"      -d '{"name":"João","email":"joao@example.com"}'
```
###  Listar usuários
```bash
curl http://localhost:5000/users
```
###  Atualizar usuário (exemplo ID=1)
```bash
curl -X PUT http://localhost:5000/users/1      -H "Content-Type: application/json"      -d '{"name":"João Silva","email":"joao.silva@example.com"}'
```
###  Excluir usuário
```bash
curl -X DELETE http://localhost:5000/users/1
```

##  Segurança
- O banco **não usa o usuário root**.  
- Usuário `usuario_app` criado com permissões limitadas.  
- Variáveis sensíveis no arquivo `.env`.  

##  Encerrar Containers
```bash
docker compose down
```
Para parar e **remover volumes** (zerar banco):
```bash
docker compose down -v
```

##  Autor
**Wilton da Silva Santos**  
Atividade: Ambiente Multi-container (Flask + MySQL + Docker Compose)
