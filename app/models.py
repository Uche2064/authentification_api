from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text
from .db import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    nom = Column(String(50), nullable=False)
    prenom = Column(String(100))
    username = Column(String(40), nullable=False, unique=True, index=True)
    email = Column(String(150), unique=True, index=True)
    adresse = Column(String(150))
    numero = Column(String(30))
    password = Column(String(256), nullable=False)
    
    date_ajout = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    date_modif = Column(TIMESTAMP(timezone=True), server_default=text("now()"))