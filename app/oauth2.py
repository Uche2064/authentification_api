from jose import jwt, JWTError
from datetime import datetime, timedelta

CLEF_SECRETE = "83c57148562ae011a9f29110&écc86dc62937382a9b'-959ace280c^mpù:;!3f1e46e764092"
ALGORITHME = "HS256"
DUREE_DE_VALIDITER = 30 


def creer_token(payload: dict) -> str:
    to_encode = payload.copy()
    
    expire = datetime.now() + timedelta(minutes=DUREE_DE_VALIDITER)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, CLEF_SECRETE, algorithm=ALGORITHME)