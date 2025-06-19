from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore


DATABASE_URL = "postgresql://postgres:1234@localhost:1234/biblioteca"

#  Conexão com o banco
engine = create_engine(DATABASE_URL)

#  Sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Base para os modelos
Base = declarative_base()
