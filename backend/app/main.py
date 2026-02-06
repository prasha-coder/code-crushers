from fastapi import FastAPI, Depends
from app.auth.router import router as auth_router
from app.auth.dependencies import get_current_user, require_admin

app = FastAPI(title="Code Crushers Backend")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "backend alive"}

@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": current_user["sub"],
        "role": current_user["role"]
    }

@app.get("/admin")
def admin_route(current_user: dict = Depends(require_admin)):
    return {
        "message": "Admin access granted",
        "user": current_user["sub"]
    }
