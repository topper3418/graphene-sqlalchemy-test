from __future__ import annotations
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from typing import List

from .base import Base
from .util import fk, rel_bp

class Person(Base):
    __tablename__ = 'people'

    name: Mapped[str]
    belongings: Mapped[List["Belonging"]] = rel_bp("person")
    favorite_locations = relationship("Location", secondary="people_location_association")
    biggest_fan: Mapped["Pet"] = rel_bp("favorite_person")


class Pet(Base):
    __tablename__ = 'pets'

    name: Mapped[str]
    favorite_person_id: Mapped[int] = fk("people.id")
    favorite_person: Mapped["Person"] = rel_bp("biggest_fan")
    # relationships
    belongings: Mapped[List["Belonging"]] = rel_bp("pet")
    favorite_locations = relationship("Location", secondary="pet_location_association")


class Location(Base):
    __tablename__ = 'locations'

    name: Mapped[str]
    people = relationship("Person", secondary="people_location_association")
    pets = relationship("Pet", secondary="pet_location_association")


class Belonging(Base):
    __tablename__ = 'belongings'

    name: Mapped[str]
    favoritePerson_id: Mapped[int] = fk("people.id")
    favoritePerson : Mapped["Person"] = rel_bp("belongings")
    pet_id: Mapped[int] = fk("pets.id")
    pet: Mapped["Pet"] = rel_bp("belongings")
    person_id: Mapped[int] = fk("people.id")
    person: Mapped["Person"] = rel_bp("belongings")



people_location_association = Table('people_location_association', Base.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)

pet_location_association = Table('pet_location_association', Base.metadata,
    Column('pet_id', Integer, ForeignKey('pets.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)