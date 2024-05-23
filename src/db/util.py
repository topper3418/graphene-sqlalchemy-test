from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship


def rel_bp(back_populates):
    return relationship(back_populates=back_populates)


def fk(ref_str: str):
    return mapped_column(ForeignKey(ref_str))