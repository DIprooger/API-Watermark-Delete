import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
load_dotenv()

_scheme = HTTPBearer(auto_error=False)
API_TOKEN = os.getenv("API_TOKEN")

def verify_token(creds: HTTPAuthorizationCredentials = Depends(_scheme)):
    if not creds or creds.scheme.lower() != "bearer" or creds.credentials != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
