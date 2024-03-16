from fastapi import APIRouter, HTTPException, status, Depends
from .. import db, models, schema, utils
from sqlalchemy.orm import Session
from sqlalchemy import or_


router = APIRouter(
    prefix="/user",
    tags=["Sign in"]
    
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.CreateResponse)
def create_user(user: schema.BaseUser, db: Session = Depends(db.get_db)):
    #  verifier si le username est deja pris ou si l'email existe deja dans notre bd
    get_user = db.query(models.Users).filter(or_(models.Users.username == user.username,  models.Users.email == user.email)).first()
    
    if get_user:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="E-mail ou username déjà pris")
    user.password = utils.hash(user.password)
    new_user = models.Users(**user.model_dump(exclude_unset=True))

    db.add(new_user)
    db.commit()
    db.refresh
    return new_user