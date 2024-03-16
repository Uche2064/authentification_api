from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CHAINE_DE_CONNEXION = "mysql://uche:KD7eMgYx@localhost:3310/auth"

moteur = create_engine(CHAINE_DE_CONNEXION)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=moteur)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()