from sqlalchemy import Integer, MetaData, String, Column

from src.database import Base


metadata = MetaData()

class HeaderMenu(Base):
    __tablename__ = 'menu_header_menu'
    metadata = metadata
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(length=255))
    url: str = Column(String(length=255))
