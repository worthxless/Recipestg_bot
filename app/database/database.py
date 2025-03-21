from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL базы данных (например, SQLite для простоты)
DATABASE_URL = "sqlite:///db/db.db"

# Создаем движок базы данных
engine = create_engine(DATABASE_URL, echo=True)

# Создаем базовый класс для моделей
Base = declarative_base()

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(engine):
    # Импортируем модели, чтобы создать таблицы
    import app.database.models.user
    import app.database.models.category
    import app.database.models.image
    import app.database.models.meal
    # Создаем все таблицы в базе данных (если они еще не созданы)
    Base.metadata.create_all(bind=engine)
