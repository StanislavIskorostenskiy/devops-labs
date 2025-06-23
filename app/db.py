from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


# Строка подключения к базе
SQLALCHEMY_DATABASE_URL = settings.database_url

# Создаём движок SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создаём фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
