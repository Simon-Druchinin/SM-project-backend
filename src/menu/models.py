from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import Column

from src.database import Base


class HeaderMenu(Base):
    __tablename__ = 'menu_header_menu'
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(length=255))
    url: str = Column(String(length=255))
