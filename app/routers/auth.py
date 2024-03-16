from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .. import db, models, oauth2, utils
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/auth",
    tags=["Authentification"]
    
)

@router.post("/login")
async def login(user: Annotated[OAuth2PasswordRequestForm, Depends()] ,db: Session = Depends(db.get_db)):
    get_user = db.query(models.Users).filter(models.Users.username == user.username).first()
    
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    
    if not utils.verifier_hash(user.password, get_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Information invalide")
    
    payload = {
        "id": get_user.id,
        "username": get_user.username,
        "email": get_user.email
    }
    token = oauth2.creer_token(payload)
    return {
        "token": token,
        "type du token": "bearer"
    }
    