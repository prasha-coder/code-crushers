from fastapi import APIRouter, HTTPException
from app.auth.schemas import UserCreate, TokenResponse
from app.core.security import hash_password, verify_password
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

fake_users = {}

@router.post("/register")
def register(user: UserCreate):
    if user.email in fake_users:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users[user.email] = hash_password(user.password)
    return {"message": "User registered"}

@router.post("/login", response_model=TokenResponse)
def login(user: UserCreate):
    stored_hash = fake_users.get(user.email)

    if not stored_hash or not verify_password(user.password, stored_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(subject=user.email)
    return {"access_token": token}
