from typing import List, ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from fastapi.templating import Jinja2Templates
from pathlib import Path

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://projects:123456@localhost:5432/etec'
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory='templates')
    MEDIA: ClassVar[Path] = Path('media')

    JWT_SECRET : str = 'nhOvPRuolDauvLj0AsXSqhDV5x8ouGQkX7Yo5qCyRK8'
    """ 
    import secrets

    token: str = secrets.token_urlsafe(32)

    token
    """

    ALOGORITHM: str = 'HS256'
    #60 minutos * 24 horas * 7 dias = 1 semana de duracao
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()