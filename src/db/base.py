from typing import Annotated
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int]


id = Annotated[int, mapped_column(primary_key=True)]
db = SQLAlchemy(model_class=Base)