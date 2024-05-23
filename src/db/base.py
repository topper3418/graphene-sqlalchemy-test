from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///database.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


id = Annotated[int, mapped_column(primary_key=True)]