from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str

class TokenResponse(BaseModel):
    access_token: str
