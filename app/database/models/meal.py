from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.database.database import Base


class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=True)
    description = Column(String(200), nullable=True)
    recipe = Column(String(4000), nullable=True)
    price = Column(Integer, nullable=True)
    image_id = Column(Integer, default=0)

    # image = relationship('Image', foreign_keys='Meal.image_id')
    cats = relationship('Category', secondary='meal_category', back_populates='meals')

    def __repr__(self) -> str:
        return f"<Meal(title={self.title}, price='{self.price}')>"



class MealCategory(Base):
    __tablename__ = 'meal_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))



class MealImage(Base):
    __tablename__ = 'meal_image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    image_id = Column(Integer, ForeignKey('images.id'))

