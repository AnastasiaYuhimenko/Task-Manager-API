from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Security

securite = HTTPBearer()


def get_token(creditials: HTTPAuthorizationCredentials = Security(securite)):
    if creditials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неправильная схема авторизации",
        )

    return creditials.credentials
