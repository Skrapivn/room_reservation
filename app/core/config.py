from typing import Optional

from pydantic import BaseSettings, EmailStr

class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'произвольное описание проекта'
    database_url: str
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
