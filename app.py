from config.database import Base, engine
from models import Autor, Livro, Cliente, Usuario, Retirada

print("🎯 Criando as tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")


