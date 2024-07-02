from typing import Optional
from pydantic import Field, HttpUrl, BaseModel as ASBaseModel

from sqlalchemy.orm import relationship

class ArtigoSchema(ASBaseModel):
    id: Optional[int] = Field(default=None)
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int] = Field(default=None)


    class Config:
        from_attributes = True