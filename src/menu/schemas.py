from pydantic import BaseModel

class HeaderMenuReadCreateSchema(BaseModel):
    id: int
    name: str
    url: str
