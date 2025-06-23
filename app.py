from fastapi import FastAPI
from config.database import Base, engine
from routes import (
    autor_routes,
    cliente_routes,
    livros_routes,
    retirada_routes,
    usuario_routes
)
from fastapi.middleware.cors import CORSMiddleware

# Criação das tabelas no banco
print("Criando as tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

# 🚀 Instanciando a aplicação
app = FastAPI(
    title="API Biblioteca",
    description="Sistema de gerenciamento de biblioteca com cadastro de livros, autores, clientes, retiradas e devoluções.",
    version="1.0.0"
)

#Configurando CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# oncluindo as rotas
app.include_router(autor_routes.router)
app.include_router(cliente_routes.router)
app.include_router(livros_routes.router)
app.include_router(retirada_routes.router)
app.include_router(usuario_routes.router)

# Rota de teste
@app.get("/")
def read_root():
    return {"mensagem": "API da Biblioteca está online 🚀"}
