class Settings:
    SECRET_KEY = "super-secret-key-change-this"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    DATABASE_URL = "postgresql://postgres:Prashant%401324@localhost:5432/code_crushers_db"

settings = Settings()
