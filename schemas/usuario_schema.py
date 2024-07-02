from typing import Optional, List
from pydantic import Field, EmailStr, BaseModel as USBaseModel

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(USBaseModel):
    id: Optional[int] = Field(default=None)
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        from_attributes = True

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[list[ArtigoSchema]]


class UssuarioSchemaUpdate(UsuarioSchemaBase):
    nome: Optional[str] = Field(default=None)
    sobrenome: Optional[str] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
    senha: Optional[str] = Field(default=None)
    eh_admin:Optional[bool] = Field(default=None)