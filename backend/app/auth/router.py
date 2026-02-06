from fastapi import APIRouter, HTTPException
from app.auth.schemas import UserCreate, TokenResponse
from app.core.security import hash_password, verify_password
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# In-memory user store (temporary)
fake_users = {}

@router.post("/register")
def register(user: UserCreate):
    if user.email in fake_users:
        raise HTTPException(status_code=400, detail="User already exists")

    # First registered user becomes admin (for demo)
    role = "admin" if len(fake_users) == 0 else "user"

    fake_users[user.email] = {
        "password": hash_password(user.password),
        "role": role
    }

    return {"message": f"User registered as {role}"}


@router.post("/login", response_model=TokenResponse)
def login(user: UserCreate):
    stored_user = fake_users.get(user.email)

    if not stored_user or not verify_password(
        user.password,
        stored_user["password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        subject=user.email,
        role=stored_user["role"]
    )

    return {"access_token": token}
