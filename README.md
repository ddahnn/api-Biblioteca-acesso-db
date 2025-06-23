API Biblioteca

Sistema de gerenciamento de uma biblioteca, desenvolvido em Python utilizando o framework FastAPI, com persistência de dados em banco de dados PostgreSQL.
Permite o controle de livros, autores, clientes, retiradas e devoluções de livros, além de autenticação de usuários.
🚀 Funcionalidades

    ✅ CRUD de Autores

    ✅ CRUD de Clientes

    ✅ CRUD de Livros

    ✅ Registro de Retiradas (com limite de 3 livros por cliente e controle de disponibilidade)

    ✅ Registro de Devoluções (com cálculo de dias de atraso)

    ✅ Autenticação de Usuário (com hash de senha)

    ✅ Busca de livros por:

        Disponibilidade

        Nome

        Autor

🛠️ Tecnologias utilizadas

    Python 3.12

    FastAPI

    SQLAlchemy

    PostgreSQL

    Pydantic v2

    Uvicorn (Servidor ASGI)

    Passlib (Criptografia de senhas)

💾 Estrutura do Projeto

.
├── app.py
├── config/
│   └── database.py
├── models/
├── routes/
├── schemas/
├── services/
├── requirements.txt
└── README.md

🏗️ Instalação e execução
🔸 1. Clone o repositório:

git clone https://github.com/seuusuario/seu-repo.git
cd seu-repo

🔸 2. Crie um ambiente virtual:

python -m venv .venv

🔸 3. Ative o ambiente:

    No Windows:

.venv\Scripts\activate

    No Mac/Linux:

source .venv/bin/activate

🔸 4. Instale as dependências:

pip install -r requirements.txt

🔸 5. Configure o banco de dados:

No arquivo config/database.py, ajuste a URL de conexão:

DATABASE_URL = "postgresql://usuario:senha@localhost:5432/biblioteca"

🔸 6. Execute a aplicação:

uvicorn app:app --reload

🔗 Acesso à documentação

    Swagger UI: http://127.0.0.1:8000/docs

    Redoc: http://127.0.0.1:8000/redoc

🗒️ Exemplos de Endpoints
🔑 Autenticação

    POST /usuarios/ — Criar usuário

    GET /usuarios/ — Listar usuários

    GET /usuarios/buscar/{username} — Buscar usuário por username

📖 Livros

    POST /livros/ — Criar livro

    GET /livros/ — Listar livros

    GET /livros/{isbn} — Buscar livro por ISBN

    DELETE /livros/{isbn} — Deletar livro

🧑 Autores

    POST /autores/

    GET /autores/

    GET /autores/{id}

    DELETE /autores/{id}

👥 Clientes

    POST /clientes/

    GET /clientes/

    GET /clientes/{matricula}

    DELETE /clientes/{matricula}

🔄 Retiradas

    POST /retiradas/ — Criar retirada

    GET /retiradas/ — Listar retiradas

    GET /retiradas/{id} — Buscar retirada por ID

    PUT /retiradas/{id}/devolver — Registrar devolução

    DELETE /retiradas/{id} — Deletar retirada


🧑‍💻 Autor

    Daniel Luis Bortolin da Silva  - Desenvolvimento de Serviços e APIS - 2025-1-noite-ADS