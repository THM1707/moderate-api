import os


class Settings:
    PROJECT_NAME: str = "My FastAPI App"
    ENV: str = os.getenv("ENV", "development")


settings = Settings()
