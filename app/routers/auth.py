from fastapi import APIRouter, HTTPException, status, Depends
from .. import db, models, schema, utils
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/auth",
    tags=["Authentification"]
    
)

@router.post("/login")
def login(user: schema.LoginUser ,db: Session = Depends(db.get_db)):
    get_user = db.query(models.Users).filter(models.Users.username == user.username).first()
    
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    
    if not utils.verifier_hash(user.password, get_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Information invalide")
    
    return {
        "token": "",
        "type du token": "bearer"
    }
    