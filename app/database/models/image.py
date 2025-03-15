from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String(100), unique=True)
    path = Column(String(100))

    def __repr__(self) -> str:
        return f"<Image(id={self.id}, path={self.path})>"


