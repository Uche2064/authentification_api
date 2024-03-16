from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(text_clair: str)->str:
    return pwd_context.hash(text_clair)


def verifier_hash(text_clair: str, text_hasher: str) -> bool:
    return pwd_context.verify(text_clair, text_hasher)