from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseUser(BaseModel):
    nom: str
    prenom: Optional[str] = None
    username: str
    email: Optional[EmailStr] = None
    adresse: str
    numero: Optional[str] = None
    password: str
    

class LoginUser(BaseModel):
    username: str
    password: str
    
class CreateResponse(BaseModel):
    id: int
    nom: str
    nom: str
    prenom: Optional[str] = None
    username: str
    email: Optional[EmailStr] = None
    adresse: str
    numero: Optional[str] = None