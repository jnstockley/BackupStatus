from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import Session

import config.config as config
from models.models import Base, Folder

ENGINE: Engine


def setup_db_connection():
    global ENGINE
    url = config.get_value("database.url")
    ENGINE = create_engine(url)
    Base.metadata.create_all(ENGINE)


def save(model: Base):
    with Session(ENGINE) as session:
        session.add(model)
        session.commit()


def get_all():
    with Session(ENGINE) as session:
        folder: Folder = session.query(Folder).first()
        print(folder.id)
