from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Substituindo PostgreSQL pelo SQLite
DATABASE_URL = "sqlite:///./example.db"  # Banco SQLite armazenado no arquivo 'example.db'

# Cria o motor do banco com SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Criar as tabelas no SQLite
def init_db():
    Base.metadata.create_all(bind=engine)
