from sqlalchemy import Column, Integer, String, Boolean

from app.database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=True)
    name = Column(String(50), nullable=True)
    surname = Column(String(50), nullable=True)
    number = Column(String(50), nullable=True)
    course = Column(Integer, nullable=True)
    isAdmin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<User(user_id={self.user_id}, username='{self.username}')>"


