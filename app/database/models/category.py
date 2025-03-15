from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref

from app.database.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    description = Column(String(50), nullable=True)

    meals = relationship('Meal', secondary='meal_category', back_populates='cats')

    def __repr__(self) -> str:
        return f"<Category(title={self.title})>"


