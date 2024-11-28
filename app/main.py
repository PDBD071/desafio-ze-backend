from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Importações corrigidas
from . import crud, models, schemas
from .database import SessionLocal, engine

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Inicializar o FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/partners/")
def create_partner(partner: schemas.PartnerCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar um parceiro.
    """
    return crud.create_partner(db=db, partner=partner)

@app.get("/partners/{partner_id}")
def read_partner(partner_id: str, db: Session = Depends(get_db)):
    """
    Endpoint para buscar um parceiro por ID.
    """
    return crud.get_partner(db, partner_id=partner_id)

@app.get("/partners/nearby")
def get_nearby_partner(latitude: float, longitude: float, db: Session = Depends(get_db)):
    """
    Endpoint para buscar parceiros próximos por coordenadas.
    """
    return crud.get_nearby_partner(db, latitude, longitude)


