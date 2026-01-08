# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Os estudantes irão construir uma API REST simples usando o framework FastAPI. A tarefa cobre definição de rotas, modelos com Pydantic, operações CRUD básicas e execução local com Uvicorn.

## 📝 Tasks

### 🛠️ Implementar API CRUD básica

#### Description
Implemente uma API para gerenciar um recurso `Item` com operações de criar, ler, atualizar e deletar (CRUD). Use `FastAPI` para rotas e `Pydantic` para validação de esquema.

#### Requirements
Completed program should:

- Expor rota `POST /items/` para criar um item
- Expor rota `GET /items/{id}` para obter um item
- Expor rota `PUT /items/{id}` para atualizar um item
- Expor rota `DELETE /items/{id}` para remover um item

### 🛠️ Testes e Execução

#### Description
Teste manualmente usando `curl` ou `HTTPie` e verifique respostas e códigos de status.

#### Requirements
Completed program should:

- Fornecer instruções claras para executar a aplicação localmente
- Retornar códigos HTTP apropriados (201, 200, 404, 400, 204)
- Validar o payload usando `Pydantic`

---

## Entregáveis

- Código fonte na pasta `assignments/fastapi-rest-apis/`
- `starter-code.py` contendo um exemplo funcional
- `requirements.txt` com dependências

## Dica

Comece rodando:

`pip install -r requirements.txt`

`uvicorn starter-code:app --reload --port 8000`

Abra `http://localhost:8000/docs` para usar a interface interativa do Swagger UI.
