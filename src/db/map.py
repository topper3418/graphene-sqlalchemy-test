from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from typing import List

from .base import db
from .util import fk, rel_bp

class Person(db.Model):
    __tablename__ = 'people'

    name: Mapped[str]
    belongings: Mapped[List["Belonging"]] = rel_bp("person")


class Pet(db.Model):
    __tablename__ = 'pets'

    name: Mapped[str]
    favorite_person_id: Mapped[int] = fk("people.id")
    favorite_person: Mapped["Person"] = rel_bp("pet")
    # relationships
    belongings: Mapped[List["Belonging"]] = rel_bp("pet")


class Location(db.Model):
    __tablename__ = 'locations'

    name: Mapped[str]


class Belonging(db.Model):
    __tablename__ = 'belongings'

    name: Mapped[str]
    favoritePerson_id: Mapped[int] = fk("people.id")
    favoritePerson : Mapped["Person"] = rel_bp("belongings")
    pet_id: Mapped[int] = fk("pets.id")
    pet: Mapped["Pet"] = rel_bp("belongings")

    favorite_locations = relationship("Location", secondary="belonging_location_association")


belonging_location_association = Table('belonging_location_association', db.metadata,
    Column('belonging_id', Integer, ForeignKey('belongings.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)