from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from coupon.config.runtime_config import RuntimeConfig

engine = create_engine(
    "mysql://{username}:{password}@{host}/{schema}".format(username=RuntimeConfig.DB_USERNAME,
                                                           password=RuntimeConfig.DB_PASSWORD,
                                                           host=RuntimeConfig.DB_HOST,
                                                           schema=RuntimeConfig.DB_SCHEMA), echo=False)


SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

