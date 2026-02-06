from fastapi import FastAPI, Depends
from app.auth.router import router as auth_router
from app.auth.dependencies import get_current_user

app = FastAPI(title="Code Crushers Backend")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "backend alive"}

@app.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": current_user
    }
